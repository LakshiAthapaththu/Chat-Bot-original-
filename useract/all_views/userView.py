from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from useract.forms import SignUpForm
from useract.models import Inquiry
from django.contrib.auth.models import User
from chatbot.models import Layers,Classes
class SignIn(View):
    temp = 'home/home.html'
    temp1 = 'registration/login.html'
    temp2 = 'adminHome/adminHome.html'
    msg = ""
    def post(self,request):
        username = request.POST.get('username')
        password=request.POST.get('password')
        staff_state = "no"
        #user1=User.objects.filter(username=username,password=password)
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['users'] = username
            if(user.is_staff):
                all_layer_objects = Layers.objects.all()
                all_class_objects = Classes.objects.all()
                return render(request, self.temp2, {'user': request.session['users'], 'layers': all_layer_objects,
                                                       'classes': all_class_objects})

            else:

                return render(request, self.temp, {'user':request.session['users']})
        else:
            msg="invalid"
            return render(request, self.temp1, {'msg':msg})
    def get(self,request):
        msg = ""
        return render(request, self.temp1,{'msg':msg})

class SignUp(View):
        form_class = SignUpForm
        temp = 'form/user_form.html'

        # add the template
        def get(self, request):
            form = self.form_class(None)
            # if user requst to make his acc return brank page
            return render(request, self.temp, {'form': form})

        def post(self, request):
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                # user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('login')

            return render(request, self.temp, {'form': form})

class viewInqury(View):
    temp = 'view history/view_history.html'
    def get(self,request):
        user_name = request.session['users']

        user_id = User.objects.get(username=user_name).pk
        object = Inquiry.objects.filter(USERNAME=user_id)
        return render(request, self.temp, {'data':user_name, 'obj':object})

