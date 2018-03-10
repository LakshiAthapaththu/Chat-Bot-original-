from django.views.generic import View
from useract.models import Inquiry
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

class viewInqury(View):
    temp = 'view history/view_history.html'
    def get(self,request):
        user_name = request.session['users']

        user_id = User.objects.get(username=user_name).pk
        object = Inquiry.objects.filter(USERNAME=user_id)
        return render(request, self.temp, {'data':user_name, 'obj':object})