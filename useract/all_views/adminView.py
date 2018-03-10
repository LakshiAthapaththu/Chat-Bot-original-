from django.shortcuts import render
from django.views.generic import View
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from useract.models import  Inquiry,Report,Authority
from chatbot.models import Layers,Classes,sets,train
import re
class getReport(View):
    temp = 'viewReport/daily_report.html'
    temp1 = 'adminHome/adminHome.html'
    def post(self,request):
        all_layer_objects = Layers.objects.all()
        all_class_objects = Classes.objects.all()

        msg2 = "invalid entry"
        if(request.POST.get('date') is None or request.POST.get('authority') is None):
            return render(request, self.temp1, {'user': request.session['users'], 'layers': all_layer_objects,
                                                   'classes': all_class_objects,'msg':msg2})
        else:
            reg = re.compile("[\d]{1,2}/[\d]{1,2}/[\d]{2}")
            date = request.POST.get('date')
            authority = request.POST.get('authority')
            new_date = ""
            if(reg.match(date)):
              for letter in date:
                    if(letter != "/"):
                        new_date = new_date + letter
              report_id = str(authority)+str(new_date)
              authorityName = Authority.objects.filter(authority_id=int(authority))
              obj = Inquiry.objects.filter(report_id=report_id)
              return render(request, self.temp, {'date':date,'authority':authorityName,'object':obj})
            else:
                return render(request, self.temp1, {'user': request.session['users'], 'layers': all_layer_objects,
                                                       'classes': all_class_objects,'msg':msg2})


class addTrainingSets(View):
    tem = "test/test.html"
    temp1 = "adminHome/adminHome.html"
    def post(self,request):
        layer = request.POST.get('layer')
        clas = request.POST.get('class')
        parent = request.POST.get('parent')
        sentence = request.POST.get('sentence')
        all_layer_objects = Layers.objects.all()
        all_class_objects = Classes.objects.all()
        msg1 = "invalid entry"
        if(layer is None or clas is None or parent is None or sentence == '' ):
            return render(request, self.temp1,
                          {'msg1': msg1, 'user': request.session['users'], 'layers': all_layer_objects,
                           'classes': all_class_objects})
        else:
            obj = sets.objects.filter(class_id_of=int(clas),layer_id_of=int(layer),parent_id=int(parent))
            set_id=None

            set_object=''
            for obje in obj:
                set_id = obje.set_id
                set_object = obje
            if set_id is not None:
                newObj = train(sentence=sentence, set_id=set_object)
                newObj.save()
                return render(request,self.tem,{'layer':layer, 'clas':clas ,'parent':parent,'sentence':sentence,'obj':obj,'msg':"yes"})
            else:
                return render(request,self.temp1,{'msg1':msg1,'user': request.session['users'], 'layers': all_layer_objects,
                                                       'classes': all_class_objects})
def PDF(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="abc.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.

    p.drawString(100, 100, "Hello world.")

    # Close the PDF object
    p.showPage()
    p.save()
    return response

