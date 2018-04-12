import re
import datetime

di = {"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}

def validBusNumber(num):
    regNum = re.compile("([a-zA-Z]{1,3}|((?!0*-)[0-9]{1,3}))-[0-9]{4}(?<!0{4})")
    returnVal = False
    if regNum.match(num):
        returnVal = True
    return returnVal


def validDate(date):
    now = datetime.datetime.now()
    year = ''
    month = ''
    day = ''
    returnVal = False
    regNum = re.compile("[\d]{2}/[\d]{2}/[\d]{4}")
    if(regNum).match(date):
        year = date[6:]
        month = date[3:5]
        day = date [0:2]
        #if year in same
        if(int(year) == int(now.year)):
            if(int(month) == int(now.month)):
                if(int(day)<=int(now.day) and int(day)>0):
                    returnVal = True
            if(int(month)< int(now.month) and int(month)>0 and int(month)<13):
                if (int(day)<=di[str(month)] and int(day)>0):
                    returnVal = True

        elif(int(year)==int(now.year-1)):
            if(int(month)==int(now.month) and int(month)<=12) :

               if(int(day)<=di[str(month)] and int(day)>0 and int(day)>=int(now.day)):
                 returnVal = True
            elif(int(month)>int(now.month)and int(month)<=12 ):
                if (int(day) <= di[str(month)] and int(day) > 0):
                  returnVal = True


    return returnVal,day,month,year

def valiTime(time,d,m,y):
    now = datetime.datetime.now()
    returnVal = False
    reg = re.compile("([01]?[0-9]|2[0-3]):[0-5][0-9]$")
    if(reg.match(time)):
        times = time.split(":")
        if(int(d) == int(now.day) and int(m) == int(now.month) and int(y) == int(now.year)):
            if(int(times[0]) == now.time().hour):
                if(int(times[1]) <= now.time().minute):
                     returnVal= True
            if(int(times[0])<now.time().hour):
                returnVal = True
        else:
            returnVal = True
    return returnVal

def validateName(name):
    returnVal = False
    reg = re.compile("[a-zA-Z\.\'\-_\s]+")
    if(reg.match(name)):
        returnVal = True
    return returnVal


