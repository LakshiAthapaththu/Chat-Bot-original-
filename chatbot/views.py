from django.shortcuts import render
from django.conf.urls import url
from django.views.generic import View
from chatbot.functions.storeSynapes import read
from chatbot.functions.chat import clasify
from chatbot.functions import storeSynapes
from . import views
from django.template import loader
from django.http import HttpResponse
from chatbot.functions.input_processing import get_all_words,give_word_bag,clean_up_sentence
import numpy
class getbag(View):
    def get(self,request):
        words = storeSynapes.readwords()
        result = give_word_bag("conductor behavior is not acceptable",words)
        temp = "tem.html"
        return render(request,temp,{'words':numpy.array(words),'result':result})

class chat(View):
    temp1 = "chat_window.html"
    temp2= "result.html"
    def get(self,request):
        return render(request, self.temp1)
    def post(self,request):
        sentence = request.POST.get('text')
        synap = read(1,0)
        result = clasify(sentence,1,0,synap[0],synap[1],list(["bus","train"]))

        return render(request, self.temp2, {'result': result,'words':synap[2]})