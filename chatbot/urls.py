from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^getbag/$',views.getbag.as_view(),name='getbag'),
url(r'^chat/$',views.chat.as_view(),name='chat')

]