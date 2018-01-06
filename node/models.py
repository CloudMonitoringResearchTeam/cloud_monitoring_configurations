from django.db import models

# Create your models here.


class Node(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    father_pk = models.IntegerField()
    ip = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    pro_conf_file_path = models.CharField(max_length=100)
    pro_alert_rule_path = models.CharField(max_length=100)
    alert_conf_file_path = models.CharField(max_length=100)