from django.db import models
from django.contrib.auth.models import User

class Authority(models.Model):
    authority_id = models.IntegerField(primary_key=True)
    authority_name=models.CharField(max_length=100)
    status = models.CharField(max_length=10000)
    e_mail=models.EmailField()
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Report(models.Model):
    report_id= models.IntegerField(primary_key=True)
    authority_id = models.ForeignKey(
    Authority,
    null=False,
    on_delete= models.CASCADE)

class Inquiry(models.Model):
    inquiry_id = models.IntegerField(primary_key=True)
    #dateTime= models.TimeField(auto_now_add=True)
    USERNAME = models.ForeignKey(
       User,
       on_delete = models.CASCADE

    )
    description = models.CharField(max_length=1000)
    add_state = models.BooleanField()
    report_id= models.ForeignKey(

        Report,
        on_delete=models.CASCADE,
        null = False

    )
