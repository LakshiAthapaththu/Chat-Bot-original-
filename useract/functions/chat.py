from chatbot.functions.chat import clasify
from chatbot.functions.storeSynapes import read
import json
from useract.functions import validate_inputs

count = 0
busList = ['AB-0522','CD-2225']
def increment():
    global count
    count+=1

def setTo(num):
    global count
    count = num
def reply(message):
    output = ""
    if(message == "hi bot" or message == "HI BOT"):
        output= "Hi! Welcome to InquaMaK...type your inquiry here"
        setTo(1)
    elif(count == 0 ):
        output = "Type hi bot to start the chat"

    elif(count == 1):
        synap =read(1,0)
        msg = clasify(message,1,0,synap[0],synap[1],list(["bus","train"]))
        if(len(msg)>1):
            output = "cannot recognize enter valid inquiry"
        else:
            output = str(msg[0][0])
            #if(str(msg[0][0]) == "bus"):
                  #output = "enter bus number"
                  #setTo(2)
            #elif(str(msg[0][0]) == "train"):
                #output = "enter train name"
                #setTo(2)
            #output = json.dumps(output)

    elif(count == 2):
        validity = validate_inputs.validBusNumber(message)
        if (validity == True and message in busList):
            output = "enter the bus route number"
            #setTo(3)
        else:
            output = "invalid bus number enter valid but number to continue"
    #3elif(count == 3):
        #pass the next catogary for identify
        #route eka valid karana tika add krnna oni
    #elif(count == 3):
        #synap = read(2, 1)
        #result = clasify(message,2,1,synap[0],synap[1],list(["conductor","passenger","route","bus itself","driver"]))
        #output = str(result[0])
    return output

