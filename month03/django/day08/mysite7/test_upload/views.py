from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def upload_view_dj(request):
    if request.method == 'GET':
        return render(request,'test_upload_dj.html')
    elif request.method == 'POST':
        username = request.POST['username']
        avatar = request.FILES['avatar']
        User.objects.create(username=username,avatar=avatar)
        return HttpResponse('---upload is ok')