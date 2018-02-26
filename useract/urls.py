from django.conf.urls import url
from . import views
from .all_views import userView
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^$',views.getLoginPage,name='login_page'),
url(r'^login/$', userView.SignIn.as_view(), name='login'),
url(r'^home/$',views.getHomePage,name = 'home'),
url(r'^logout/$', auth_views.logout, {'template_name': 'registration/login.html'}, name='logout'),
url(r'^register/$',userView.SignUp.as_view(),name='register'),
url(r'^viewhistory/$',userView.viewInqury.as_view(),name='viewhistory')
        ]