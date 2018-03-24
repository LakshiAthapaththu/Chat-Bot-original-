
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from chatbot.models import  Classes,Layers
from .models import Inquiry

#def getLoginPage(request):
    #template = loader.get_template('loginPage/login.html')
    #return HttpResponse(template.render(request))

def getHomePage(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render(request))

class getAdminPage(View):
    template = 'adminHome/adminHome.html'
    def post(self,request):
        all_layer_objects = Layers.objects.all()
        all_class_objects = Classes.objects.all()
        return render(request, self.template, {'user': request.session['users'], 'layers': all_layer_objects,
                                                   'classes': all_class_objects})
    def get(self,request):
        all_layer_objects = Layers.objects.all()
        all_class_objects = Classes.objects.all()
        return render(request, self.template,{'user':request.session['users'],'layers':all_layer_objects,
                                              'classes':all_class_objects})



def viewReport(request):
    template = loader.get_template('viewReport/daily_report.html')
    return HttpResponse(template.render(request))

def getChatWindow(request):
    template = loader.get_template('chatWindow/chatWindow.html')
    return HttpResponse(template.render(request))



