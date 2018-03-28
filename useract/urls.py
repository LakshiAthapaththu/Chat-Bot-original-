from django.conf.urls import url
from . import views
from .all_views import userView,adminView,customerView
from django.contrib.auth import views as auth_views

urlpatterns = [
#url(r'^$',views.getLoginPage,name='login_page'),
url(r'^login/$', userView.SignIn.as_view(), name='login'),
url(r'^home/$',views.getHomePage,name = 'home'),
url(r'^logout/$', auth_views.logout, {'template_name': 'registration/login.html'}, name='logout'),
url(r'^register/$',userView.SignUp.as_view(),name='register'),
url(r'^viewhistory/$',customerView.viewInqury.as_view(),name='viewhistory'),
url(r'^admin/$',views.getAdminPage.as_view(),name = 'adminpage'),
#url(r'^report/getPDF/$',adminView.PDF ,name = 'getPDF'),
url(r'^viewreport/$',adminView.getReport.as_view(),name= 'viewreport'),
url(r'^addData/$',adminView.addTrainingSets.as_view(),name= 'addData'),
#url(r'^report/$',adminView.checkButton.as_view(),name='reports')
url(r'^edit/$',customerView.editDetails.as_view(),name='editDetails'),
url(r'^chatWindow/$',views.getChatWindow,name='chatWindow'),
    #get the chatwindow remove later
url(r'^get/$',customerView.getpage,name='get'),
url(r'^test/$',customerView.testing,name='test'),
]

