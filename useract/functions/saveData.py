import datetime
from useract.models import Report,User,Inquiry

def saveInq(user,inquiry,authority):
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    date = str(now.day)
    if(len(month) != 2):
        month = "0"+month

    if(len(date) !=2):
        date = "0"+date

    rep_id = date+month+year
    if(authority == 1):
        rep_id = str(1)+rep_id

    if(authority == 2):
        rep_id = str(2) + rep_id

    #get relevant report object
    report = Report.objects.filter(report_id = int(rep_id))
    report_obj_for_save = ''
    for rep_object in report:
        report_obj_for_save = rep_object

    #get relavant user object
    user_obj = User.objects.filter(username=user)
    user_for_save = ''
    for u in user_obj:
        user_for_save = u


    #save_obj = Inquiry(USERNAME=user_for_save , description=str(inquiry),add_state=False,report_id=report_obj_for_save)
    #save_obj.save()

    return rep_id,user