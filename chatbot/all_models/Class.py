from django.db.models import CharField, Model
from django.db import models

class Classes(models.Model):
    class_id= models.IntegerField(primary_key=True)
    class_name=models.CharField(max_length=100)