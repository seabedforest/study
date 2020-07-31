import html
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from tools.logging_dec import logging_check, get_user_by_request
from user.models import UserProfile
from topic.models import Topic


# 10300-10399
# Create your views here.
class TopicView(View):

    def make_topics_res(self, author, author_topics):
        res = {'code': 200, 'data': {}}
        topics_res = []
        for topic in author_topics:
            d = {}
            d['id'] = topic.id
            d['title'] = topic.title
            d['category'] = topic.category
            d['introduce'] = topic.introduce
            d['created_time'] = topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
            d['author'] = author.nickname
            topics_res.append(d)
        res['data']['topics'] = topics_res
        res['data']['nickname'] = author.nickname
        return res

    #@cache_page()
    def get(self, request, author_id):
        # /v1/topics/haha
        # 获取博客列表
        # 1.访问者 -visitor
        # 2.博主 - author
        try:
            author = UserProfile.objects.get(username=author_id)
        except Exception as e:
            result = {'code': 10303, 'error': 'The author is not existed!'}
            return JsonResponse(result)
        visitor_username = get_user_by_request(request)
        category = request.GET.get('category')
        filter_category = False
        if category in ['tec', 'no-tec']:
            # 判断是否符合要求
            filter_category = True

        if visitor_username == author.username:
            # 博主访问自己的博客,可获取  公开+私人的内容
            if filter_category:
                author_topics = Topic.objects.filter(author_id=author_id, category=category)
            else:
                author_topics = Topic.objects.filter(author_id=author_id)
        else:
            # 非博主访问，只获取公开内容
            if filter_category:
                author_topics = Topic.objects.filter(author_id=author_id, limit='public', category=category)
            else:
                author_topics = Topic.objects.filter(author_id=author_id, limit='public')
        res = self.make_topics_res(author, author_topics)
        return JsonResponse(res)

    @method_decorator(logging_check)
    def post(self, request, author_id):
        # 发表博客
        author = request.myuser
        json_str = request.body
        json_obj = json.loads(json_str)

        title = json_obj['title']
        # 防止xss注入
        title = html.escape(title)
        content = json_obj['content']
        # #根据提交的纯文本内容，切割30个字作为简介
        content_text = json_obj['content_text']
        introduce = content_text[:30]

        limit = json_obj['limit']
        if limit not in ['public', 'private']:
            result = {'code': 10300, 'error': 'Please give me right limit'}
            return JsonResponse(result)
        category = json_obj['category']
        # TODO 检查同上
        # 存储数据
        Topic.objects.create(title=title, content=content, limit=limit, category=category, introduce=introduce,
                             author=author)
        # return JsonResponse({'code':200,'username':'xxxx'})
        return JsonResponse({'code': 200, 'username': author.username})
