# -- coding: utf-8 --
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import hashlib
import json
# Create your views here.
from .models import User


def curlmd5(src):
    m = hashlib.md5()
    m.update(src.encode('utf-8'))
    return m.hexdigest()


def convert_to_dicts(objs):
    obj_arr = []

    for o in objs:
        # 把Object对象转换成Dict
        dict = {}
        dict.update(o.__dict__)
        dict.pop("_state", None)  # 去除掉多余的字段
        obj_arr.append(dict)

    return obj_arr


@csrf_exempt
def create_or_get_single(request):
    if request.method == 'POST':
        # create a new user
        username = request.POST['username']
        password = curlmd5(request.POST['password'])
        user = User(username=username, password=password)
        user.save()
        return HttpResponse("Creating user %s successful" % user.username, status=201)
    elif request.method == 'GET':
        # get a user information
        # data = serializers.serialize("json", User.objects.all())
        user_id = request.GET['user_id']
        data = get_list_or_404(User, pk=user_id)
        return HttpResponse(convert_to_dicts(data), status=200)


@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        # body = json.loads(request.body.decode("utf-8"))
        # password = curlmd5(body['password'])
        user_id = request.GET['user_id']
        password = curlmd5(request.POST['password'])
        user = get_object_or_404(User, id=user_id)
        user.password = password
        user.save()
        return HttpResponse("Changing password %s successful" % user.username, status=200)


# def get_single(request):
#     user = request.GET['user_id']
#     data = convert_to_dicts(User.objects.filter(id=user_id))
#     return HttpResponse(data)


# @csrf_exempt
# def create_or_get_all(request):
#     if request.method == 'POST':
#         # create a new user
#         body = json.loads(request.body.decode("utf-8"))
#         username = body['username']
#         password = curlmd5(body['password'])
#
#         user = User(username=username, password=password)
#         user.save()
#         return HttpResponse("Creating user %s successful" % user.username)
#     elif request.method == 'GET':
#         # get all user information
#         data = serializers.serialize("json", User.objects.all())
#         return HttpResponse(data)