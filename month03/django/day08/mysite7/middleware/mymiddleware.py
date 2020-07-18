from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re


class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print('---MyMW process_request do---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('---MyMW process_view do---')

    def process_response(self, request, response):
        print('---MyMW process_response do---')
        return response


class MyMW2(MiddlewareMixin):
    def process_request(self, request):
        print('---MyMW2 process_request do---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('---MyMW2 process_view do---')

    def process_response(self, request, response):
        print('---MyMW2 process_response do---')
        return response


class VisitLimit(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        # /test_mw -> /test开头的地址，都要限制
        if not re.match(r'^/test', request.path_info):
            return
        times = self.visit_times.get(ip_address, 0)
        print('IP:%s 已经访问 %s 次' % (ip_address, times))
        if times >= 5:
            return HttpResponse('---对不起 您访问次数已达上限')
        self.visit_times[ip_address] = times + 1
