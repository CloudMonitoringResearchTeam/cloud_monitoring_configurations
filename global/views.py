from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from node.models import Node
from django.shortcuts import get_object_or_404
import paramiko
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.

def ssh_connect(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, username, password)
    return ssh


def global_view(request):
    return render(request, 'global/global.html')

@csrf_exempt
def conf_file(request):
    if request.method == 'GET':

        category = request.GET['file_type']
    elif request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        category = body['filetype']
    print(category)
    if category == 'prometheus_file':
        print('p')
        return read_or_write_prometheus_conf_file(request)
    elif category == 'alert_rules':
        return read_or_write_alert_rule(request)
    elif category == 'alert_file':
        print('ff')
        return read_or_write_alert_conf_file(request)

@csrf_exempt
def read_or_write_prometheus_conf_file(request):
    if request.method == 'GET':

        node = get_object_or_404(Node, category='global')

        # t = paramiko.Transport(("101.132.171.59", 22))
        # t.connect(username="root", password="Cloud410")
        ssh = ssh_connect(node.ip, node.username, node.password)
        command = "cat " + node.pro_conf_file_path
        stdin, stdout, stderr = ssh.exec_command(command)
        data = stdout.read()

        ssh.close()

        return HttpResponse(data, status=200)

    elif request.method == 'POST':
        prometheus_conf_file = request.POST['conf_file']
        node = get_object_or_404(Node, category='global')
        ssh = ssh_connect(node.ip, node.username, node.password)
        command = "echo \"" + prometheus_conf_file + "\" > " + node.pro_conf_file_path
        print(command)
        stdin, stdout, stderr = ssh.exec_command(command)

        if stderr:
            return HttpResponse("prometheus file change failed", status=400)
        else:
            return HttpResponse("prometheus file change success", status=200)


def read_or_write_alert_rule(request):
    if request.method == 'GET':
        node = get_object_or_404(Node, category='global')
        ssh = ssh_connect(node.ip, node.username, node.password)
        command = "cat " + node.pro_alert_rule_path
        stdin, stdout, stderr = ssh.exec_command(command)
        data = stdout.read()
        ssh.close()
        return HttpResponse(data, status=200)
    elif request.method == 'POST':
        print('hello')
        body = json.loads(request.body.decode("utf-8"))
        alert_rules = body['conf_file']
        node = get_object_or_404(Node, category='global')
        ssh = ssh_connect(node.ip, node.username, node.password)
        command = "echo \"" + alert_rules + "\" > " + node.pro_alert_rule_path
        stdin, stdout, stderr = ssh.exec_command(command)
        ssh.close()
        # if stderr:
        #     return HttpResponse("alert rules file change failed", status=400)
        # else:
        return HttpResponse("alert rules file change success", status=200)

def read_or_write_alert_conf_file(request):
    print(request.method)
    if request.method == 'GET':

        node = get_object_or_404(Node, category='global')
        ssh = ssh_connect(node.ip, node.username, node.password)
        command = "cat " + node.alert_conf_file_path
        stdin, stdout, stderr = ssh.exec_command(command)
        data = stdout.read()
        print(data)
        ssh.close()
        return HttpResponse(data, status=200)
    elif request.method == 'POST':
        print('hello')
        body = json.loads(request.body.decode("utf-8"))
        alert_file = body['conf_file']
        node = get_object_or_404(Node, category='global')
        ssh = ssh_connect(node.ip, node.username, node.password)
        command = "echo \"" + alert_file + "\" > " + node.alert_conf_file_path
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout)
        if stderr:
            return HttpResponse("prometheus file change failed", status=400)
        else:
            return HttpResponse("prometheus file change success", status=200)