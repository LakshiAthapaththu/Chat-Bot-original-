from django.contrib import admin
from .models import Inquiry,Authority,Report

# Register your models here.
admin.site.register(Inquiry)
admin.site.register(Authority)
admin.site.register(Report)
#admin.site.register(UserDetails)

