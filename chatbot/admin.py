
from django.contrib import admin
from .models import train,Classes,Layers,Synapsys,sets

# Register your models here.
admin.site.register(train)
admin.site.register(Classes)
admin.site.register(Layers)
admin.site.register(Synapsys)
admin.site.register(sets)

