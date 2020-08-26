from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from alipay import AliPay
from django.conf import settings

app_private_key_string = open(settings.ALIPAY_KEY_DIRS + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIRS + 'alipay_public_key.pem').read()

ORDER_STATIC = 0  # 0:未付款 1:已付款 2：付款失败


class MyAliPay(View):
    def __init__(self, **kwarges):
        super().__init__(**kwarges)
        self.alipay = AliPay(
            appid=settings.ALIPAY_APP_ID,
            app_notify_url=None,
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
            sign_type='RSA2',
            debug=True,  # 代表为测试，该模式下 接口地址为 沙箱地址，默认是False
        )

    def get_tarde_url(self, order_id, amount):
        # 生成支付地址
        # 支付地址为  https://openapi.alipaydev.com/gateway.do?+查询字符串
        order_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount=amount,
            subject=order_id,
            return_url=settings.ALIPAY_RETURN_URL,  # 支付完毕后，支付宝将用户跳转到商户的地址
            notify_url=settings.ALIPAY_NOTIFY_URL,  # 支付结果回调地址 POST
        )
        return "https://openapi.alipaydev.com/gateway.do?" + order_string

    def get_trade_result(self, order_id):
        # 主动查询支付宝
        result = self.alipay.api_alipay_trade_query(out_trade_no=order_id)
        # trade_status - "TRADE_SUCCESS" 支付成功
        if result.get('trade_status') == "TRADE_SUCCESS":
            return True
        return False

    def get_verify_result(self, data, sign):
        # 获取验签结果， 验签 - 校验信息来源，信息是否被篡改
        # verify方法  返回值  True - 签名合法 False 非法签名
        return self.alipay.verify(data, sign)


class OrderView(MyAliPay):

    def get(self, request):
        # 获取打赏页面
        return render(request, 'order.html')

    def post(self, request):
        # 获取支付地址
        order_id = '101012389135'
        ammount = 999
        pay_url = self.get_tarde_url(order_id, ammount)
        return JsonResponse({'pay_url': pay_url})


class ResuktView(MyAliPay):
    def get(self, request):
        # return url
        order_id = request.GET.get('out_trade_no')
        # 查询库中的订单状态
        if ORDER_STATIC == 1:
            return HttpResponse('订单支付成功')
        else:
            # 主动向支付宝发请求查询订单情况
            is_success = self.get_trade_result(order_id)
            if is_success:
                print('主动查询  更改订单状态')
                # ORDER_STATUS = 1
                return HttpResponse('主动查询 订单支付成功')
            else:
                return HttpResponse('支付没成功')

    def post(self, request):
        # notify_url
        # 支付宝 会将订单的最终结果  通过post表单提交 发送至notify_url
        # request.POST 所有参数拿出  组成字典
        request_data = {k: request.POST[k] for k in request.POST.keys()}
        print('POST data is', request_data)
        sign = request_data.pop('sign')
        # 验证签名
        result = self.get_verify_result(request_data, sign)
        if result:
            # 根据具体交易结果 修改订单
            trade_status = request_data['trade_status']
            if trade_status == "TRADE_SUCCESS":
                # 支付成功
                # 变更 数据库  订单表  订单状态
                print('-----支付成功 POST---')
                # ORDER_STATIC =1
                # 注意 返回值  必须是success
        else:
            # 验签失败
            print('----验签失败----')

        return HttpResponse('success')
        # 根据具体交易结果 修改订单
