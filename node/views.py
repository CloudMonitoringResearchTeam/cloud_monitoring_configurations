from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Node
from django.shortcuts import get_object_or_404
import paramiko
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Count


def convert_to_dicts(objs):
    obj_arr = []

    for o in objs:
        # 把Object对象转换成Dict
        dict = {}
        dict.update(o.__dict__)
        dict.pop("_state", None)  # 去除掉多余的字段
        obj_arr.append(dict)

    return obj_arr





def index(request):
    return render(request, 'node/Node.html')


def add_node_view(request):
    return render(request, 'node/AddNode.html')


@csrf_exempt
def get_all_nodes(request):
    output= Node.objects.values('category').annotate(count=Count('category'))
    resp= {
        output[0]['category']:output[0]['count'],
        output[1]['category']:output[1]['count'],
        output[2]['category']:output[2]['count']
    }
    print(resp)
    return HttpResponse(json.dumps(resp), status=200)


@csrf_exempt
def get_father_pk(request):
    body = json.loads(request.body.decode("utf-8"))
    category = body['category']
    if category == 'cluster':
        node = get_object_or_404(Node, category='global')
        resp = [{'father_pk': node.pk}]
        return JsonResponse(resp, safe=False)
    elif category == 'work':
        nodes = Node.objects.filter(category='cluster')
        resp = []
        print(nodes)
        for node in nodes:
            resp.append({'father_pk': node.pk})
        return JsonResponse(resp, safe=False)


@csrf_exempt
def create_or_delete(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        category = body['category']
        name = body['name']
        ip = body['ip']
        username = body['username']
        password = body['password']
        father_pk = body['father_pk']
        pro_conf_file_path = body['prometheus_file']
        pro_alert_rule_path = body['alert_rule']
        alert_conf_file_path = body['alert_file']
        if category == 'global':
            try:
                question = Node.objects.get(category=category)
            except Node.DoesNotExist:
                node = 0
            if node:
                return HttpResponse("system has already a global node", status=400)
            else:
                father_pk = 0
                Node.objects.create(name=name, category=category, father_pk=father_pk, ip=ip,
                                    username=username, password=password,
                                    pro_conf_file_path=pro_conf_file_path,
                                    pro_alert_rule_path=pro_alert_rule_path,
                                    alert_conf_file_path=alert_conf_file_path)
                return HttpResponse("global node create success", status=201)
        elif category == 'cluster' or category == 'work':
            Node.objects.create(name=name, category=category, father_pk=father_pk, ip=ip,
                                username=username, password=password,
                                pro_conf_file_path=pro_conf_file_path,
                                pro_alert_rule_path=pro_alert_rule_path,
                                alert_conf_file_path=alert_conf_file_path)
            return HttpResponse("node create success", status=201)
    elif request.method == 'DELETE':
        body = json.loads(request.body.decode("utf-8"))
        fail_node = []
        for node in body:
            delete_node = Node.objects.filter(id=node['node_id'])
            if len(delete_node) == 0:
                fail_node.append(node)
            else:
                delete_node.delete()
        if len(fail_node) == 0:
            return HttpResponse(status=204)
        else:
            return HttpResponse(json.dumps(fail_node), status=400)
    elif request.method == 'GET':
        data = serializers.serialize("json", Node.objects.all())
        print(data)
        return HttpResponse(data)


