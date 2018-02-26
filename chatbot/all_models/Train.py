

from django.db import models
from .Class import Classes
from .Layer import Layers
class train(models.Model):
    sen_id= models.IntegerField(primary_key=True)
    sentence= models.CharField(max_length=100000)
    class_id= models.ForeignKey(
        Classes,
        on_delete = models.CASCADE
    )
    layer_id=models.ForeignKey(
        Layers,
        on_delete=models.CASCADE
    )

    class_bag=models.CharField(max_length=100000000, null=True)
    word_bag=models.CharField(max_length=100000000, null=True)

