from django.db import models
class Synapsys(models.Model):
    syn_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    data_array = models.CharField(max_length=500)