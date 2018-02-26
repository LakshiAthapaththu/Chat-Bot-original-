
from django.template import loader
from django.http import HttpResponse

#from forms inport the class
from django.contrib.auth.models import User

def getLoginPage(request):
    template = loader.get_template('loginPage/login.html')
    return HttpResponse(template.render(request))



