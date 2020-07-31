import base64
import json, hmac, copy, time


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=300):
        # init header
        header = {'typ': 'JWT', 'alg': 'HS256'}
        # sort_keys 让json串中的key有序排列
        # separators -分隔符 - 值为元组
        # 第一个值为 键值对之间靠什么分隔，第二个值为 key和value之间拿什么分隔
        header_json = json.dumps(header, sort_keys=True, separators=(',', ':'))
        header_bs = Jwt.b64encode(header_json.encode())

        # init payload
        npayload = copy.deepcopy(payload)
        npayload['exp'] = time.time() + exp
        payload_json = json.dumps(npayload, sort_keys=True, separators=(',', ':'))
        payload_bs = Jwt.b64encode(payload_json.encode())

        # init sign
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        hm_bs = Jwt.b64encode(hm.digest())
        return header_bs + b'.' + payload_bs + b'.' + hm_bs

    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    @staticmethod
    def b64decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
        return base64.urlsafe_b64decode(b_s)

    @staticmethod
    def decode(token, key):
        # 校验签名 - raise
        header_bs, payload_bs, sign_bs = token.split(b'.')
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        if sign_bs != Jwt.b64encode(hm.digest()):
            raise Exception('签名不对')
            # 比对时间 - raise
        # 替换的等号部回来
        payload_js = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_js)
        exp = payload['exp']
        now = time.time()
        if now > exp:
            # token过期
            raise Exception('token过期')
            # 返回payload字典
        return payload


if __name__ == '__main__':
    s = Jwt.encode({'uname': 'hailin'}, 'koko')
    print(s)
    # time.sleep(4)
    payload = Jwt.decode(s, 'koko')
    print(payload)
