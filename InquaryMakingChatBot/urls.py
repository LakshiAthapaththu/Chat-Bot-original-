from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #if give url like admin/ goto the admin page
    url(r'^useract/',include('useract.urls')),
    url(r'^bot/',include('chatbot.urls')),

]
