from django.shortcuts import render
from django.conf.urls import url
from . import views
from django.template import loader
from django.http import HttpResponse
from chatbot.addSets import abc,makeBags
def add(request):
    #abc(1,"how are you?",1,1)
    #abc(2, "how is your day?",1, 1)
    #abc(3, "good day", 1, 1)
    #abc(4, "how is it going today?", 1, 1)
    #abc(5, "have a nice day",2, 1)
    #abc(6, "see you later", 2, 1)
    #abc(7, "have a nice day",2, 1)
    #abc(8, "talk to you soon",2, 1)
    #abc(9, "make me a sandwich", 3, 1)
    #abc(10, "can you make a sandwich?", 3, 1)
    #abc(11, "having a sandwich today?", 3, 1)
    #abc(12, "what's for lunch?", 3, 1)
    template = loader.get_template('tem.html')
    context = {
            'all': makeBags(),

        }
    return HttpResponse(template.render(context, request))


    #return HttpResponse("<h1>"++"</h1>")