from django.db.models import CharField, Model
from django.db import models

class Layers(models.Model):
    layer_id=models.IntegerField(primary_key=True)
    layer_name=models.CharField(max_length=100)