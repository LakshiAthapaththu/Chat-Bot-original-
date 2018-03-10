
from django.db import models
class Classes(models.Model):
    class_id= models.AutoField(primary_key=True)
    class_name=models.CharField(max_length=100)

class Layers(models.Model):
    layer_id=models.AutoField(primary_key=True)
    layer_name=models.CharField(max_length=100)

class sets(models.Model):
    set_id = models.AutoField(primary_key=True)
    class_id_of = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE
    )
    layer_id_of = models.ForeignKey(
        Layers,
        on_delete=models.CASCADE
    )
    parent_id = models.IntegerField(null=False)

class train(models.Model):
    sentence_id= models.AutoField(primary_key=True)
    sentence= models.CharField(max_length=100000)
    set_id= models.ForeignKey(
        sets,
        on_delete = models.CASCADE
    )
    class_bag=models.CharField(max_length=100000000, null=True)
    word_bag=models.CharField(max_length=100000000, null=True)

class Synapsys(models.Model):
    syn_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    data_array = models.CharField(max_length=500)
