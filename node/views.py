from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .models import Node
from django.shortcuts import get_object_or_404
import paramiko
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


def convert_to_dicts(objs):
    obj_arr = []

    for o in objs:
        # 把Object对象转换成Dict
        dict = {}
        dict.update(o.__dict__)
        dict.pop("_state", None)  # 去除掉多余的字段
        obj_arr.append(dict)

    return obj_arr


def ssh_connect(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, username, password)
    return ssh


def index(request):
    return render(request, 'user/')


@csrf_exempt
def get_father_pk(request):
    body = json.loads(request.body.decode("utf-8"))
    category = body['category']
    if category == 'cluster':
        node = get_object_or_404(Node, category='global')
        resp = {'father_pk': node.father_pk}
        return JsonResponse(resp, safe=False)
    elif category == 'work':
        nodes = Node.objects.filter(category='cluster')
        resp = []
        print(nodes)
        for node in nodes:
            resp.append(node.pk)
        return JsonResponse(resp, safe=False)


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
            node = get_object_or_404(Node, category='global')
            if node:
                HttpResponse("system has already a global node", status=400)
            else:
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
        node_id = body['node_id']
        Node.objects.filter(id=node_id).delete()
        return HttpResponse(status=204)

@csrf_exempt
def read_or_write_prometheus_conf_file(request):
    if request.method == 'GET':
        node_id = request.GET['node_id']
        node = get_object_or_404(Node, pk=node_id)
        # t = paramiko.Transport(("101.132.171.59", 22))
        # t.connect(username="root", password="Cloud410")
        ssh = ssh_connect(node.ip, node.username, node.password)
        command = "cat "+node.pro_conf_file_path
        stdin, stdout, stderr = ssh.exec_command(command)
        data = stdout.read()
        ssh.close()
        return HttpResponse(data, status=200)
    elif request.method == 'POST':
        node_id = request.GET['node_id']
        prometheus_conf_file = request.POST['conf_file']
        print(prometheus_conf_file)
        node = get_object_or_404(Node, pk=node_id)
        ssh = ssh_connect(node.ip, node.username, node.password)
        command = "echo \""+prometheus_conf_file+"\" > "+node.pro_conf_file_path
        print(command)
        stdin, stdout, stderr = ssh.exec_command(command)

        if stderr:
            return HttpResponse("prometheus file change failed", status=400)
        else:
            return HttpResponse("prometheus file change success", status=200)


def read_or_write_alert_rule(request):
    if request.method == 'GET':
        node_id = request.GET['node_id']
        node = get_object_or_404(Node, pk=node_id)
        ssh = ssh_connect()
        command = "cat "+node.pro_alert_rule_path
        stdin, stdout, stderr = ssh.exec_command(command)
        data = stdout.read()
        ssh.close()
        return HttpResponse(data, status=200)


def read_or_write_alert_conf_file(request):
    if request.method == 'GET':
        node_id = request.GET['node_id']
        node = get_object_or_404(Node, pk=node_id)
        ssh = ssh_connect()
        command = "cat "+node.alert_conf_file_path
        stdin, stdout, stderr = ssh.exec_command(command)
        data = stdout.read()
        ssh.close()
        return HttpResponse(data, status=200)