from chatbot.functions.chat import clasify
from chatbot.functions.storeSynapes import read
import json
from useract.functions import saveData
import datetime



from useract.functions import validate_inputs
catogary1 = ''
catogary2 = ''
count = 0
busList = ['AB-0522','CD-2225']
trainList = ["Ruhunu Kumari", "Udarata Manike"]
year = ''
month = ''
day = ''
date = ''
time = ''
inquiry = ''
previous_count= ''

def setPreCount(c):
    global  previous_count
    previous_count = c

def setTo(num):
    global count
    count = num

def setCat1(catogary):
    global catogary1
    catogary1 = catogary

def setCat2(catogary):
    global catogary2
    catogary2 = catogary

def setDate(d,m,y):
    global day
    global month
    global year
    day = d
    month = m
    year = y

def setInquiry(inq):
    global inquiry
    inquiry += inq

def clearInr():
    global inquiry
    inquiry = ''

#get user input process and pass the reply
def reply(message,user):
  output = ""
  while(True):
    #start
    if(count == 0):
        clearInr()
        if(message.lower() == "hi bot"):
            output= "Hi! Welcome to InquaMaK...type your inquiry here"
            setTo(1)

        else:
            output = "Error! Type 'hi bot' to start the chat"
        break

    #work with user inquiry (inconvenences or problems)
    elif(count == 1):
        synap =read(1,0)
        msg = clasify(message,1,0,synap[0],synap[1],list(["bus","train"]))
        if(len(msg)>1 or len(msg) == 0):
            setPreCount(count)
            output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
            setTo(7)

        else:

            if(str(msg[0][0]) == "bus"):
                  output = "enter bus number"
                  setTo(2)
                  setInquiry("Inquiry: "+message+'<br>')
                  setCat1("bus")

                  #catogorize furture
                  synap = read(2, 1)
                  cat2 =  clasify(message,2,1,synap[0],synap[1],list(["conductor","passengers","route","busitself","driver"]))
                  if(len(cat2)>1 or len(cat2) == 0):
                      setCat2('')
                  else:
                      setCat2(str(cat2[0][0]))

            elif(str(msg[0][0]) == "train"):
                output = "enter train name"
                setTo(2)
                setInquiry("Inquiry: "+message+'<br>')
                setCat1("train")
                synap = read(2, 2)
                cat2 = clasify(message, 2, 2, synap[0], synap[1],
                               list(["passenger", "route", "trainitself","driver"]))
                if (len(cat2) > 1 or len(cat2) == 0):
                    setCat2('')
                else:
                    setCat2(str(cat2[0][0]))

        break

    #get the date and valid inquiry
    elif(count == 2 ):
       if(catogary1 == "bus"):
            validity = validate_inputs.validBusNumber(message)
            if (validity == True):
                if(message in busList):
                    output = "enter the date you faced the inconvenience"
                    setTo(3)


                else:
                    setPreCount(count)
                    output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
                    setTo(7)


            else:
                setPreCount(count)
                output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
                setTo(7)



       elif(catogary1 == "train"):
           if ( message in trainList):
               output = "enter the date you faced the inconvenience"
               setTo(3)


           else:
               setPreCount(count)
               output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
               setTo(7)
       break
    #valid date and ask goe time
    elif (count == 3):
       now = datetime.datetime.now()
       date = message
       dateValidity = validate_inputs.validDate(str(date))
       if(dateValidity[0] == True):
           output = "enter the time you faced the inconvenience"
           setInquiry("Date: "+message+'<br>')
           setDate(dateValidity[1],dateValidity[2],dateValidity[3])
           setTo(4)

       else:
           setPreCount(count)
           output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
           setTo(7)
       break

    #show full inquiry and ask goe confirmation
    elif(count == 4):
        time = message
        validity = validate_inputs.valiTime(time,day,month,year)
        if(validity == True):
            setInquiry("Time: "+message)

            #output = inquiry+'<br>'+'<br>'+"Confirm the Inquiry(yes/no)"
            if(catogary2 != ''):
                output = getOutPut(catogary2,catogary1)
                if(output != ''):
                  setTo(5)
                  break
                else:
                    setTo(8)

            else:
                output = inquiry + '<br>' + '<br>' + "Confirm the Inquiry(yes/no)"
                setTo(6)
                break

        else:
            setPreCount(count)
            output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
            setTo(7)
            break


    #ask for confirmation
    elif(count == 5):
      if(message.lower() != 'ignore' and message != ''):
        #validate a name of driver or conductor
        if (catogary2 == 'conductor' or catogary2 == "driver"):
            if(validate_inputs.validateName(message)):
               setInquiry(message)
            else:
                setPreCount(count)
                output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
                setTo(7)
                break
        elif(message == ''):
            setPreCount(count)
            output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
            setTo(7)
            break

        else:
            setInquiry(message)

      else:
          setInquiry("not known")
      output = inquiry+'<br>'+'<br>'+"Confirm the Inquiry(yes/no)"
      setTo(6)
      break

    elif(count == 8):
        output = inquiry + '<br>' + '<br>' + "Confirm the Inquiry(yes/no)"
        setTo(6)
        break

    elif(count == 6):
        if(message.lower() == 'yes'):
            output = saveData.saveInq(user,inquiry,1)
            #save the inquiry
            #if (catogary1 == 'bus'):

                #saveData.saveInq(user,inquiry,1)
            #elif(catogary1 == 'train'):
                #saveData.saveInq(user,inquiry,2)
            clearInr()
            setTo(0)
        elif(message.lower() == 'no'):
            output = "recording has been canceled"
            clearInr()
            setTo(0)
        else:
            setPreCount(count)
            output = "Invalid Input! Type 'cancel' to cancel the recording and see the user guidance"
            setTo(7)
        break


    #work with cancelations and retries
    elif(count == 7):
        if(message.lower() == 'cancel' ):
            clearInr()
            setTo(0)
            output = 'recording has been canceled'
            break
        else:
            setTo(previous_count)



  return output



#get relavant out put according to the catogary
def getOutPut(msg,cato1):
    if(cato1 == 'bus'):
        if(msg == 'conductor'):
            setInquiry('<br> Conductor Name:')
            return 'enter conductor name if you do not know type "ignore"'
        elif(msg == 'driver'):
            setInquiry('<br> Driver Name:')
            return 'enter driver name if you do not know type "ignore"'
        elif(msg == 'busitself'):
            return ''

        elif(msg == 'route'):
            setInquiry('<br> Location:')
            return 'where you faced the inconvenience if you do not know type "ignore"'

        elif(msg == 'passenger'):
            return ''

        else:
            return ''

    if (cato1 == 'train'):
        if (msg == 'driver'):
            setInquiry('<br> Driver Name:')
            return 'enter driver name if you do not know type "ignore"'
        elif (msg == 'trainitself'):
            return ''

        elif (msg == 'route'):
            setInquiry('<br> Location:')
            return 'where you faced the inconvenience if you do not know type "ignore"'

        elif (msg == 'passenger'):
            return ''

        else:
            return ''