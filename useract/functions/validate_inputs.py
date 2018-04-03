import re


def validBusNumber(num):
    regNum = re.compile("([a-zA-Z]{1,3}|((?!0*-)[0-9]{1,3}))-[0-9]{4}(?<!0{4})")
    returnVal = False
    if regNum.match(num):
        returnVal = True
    return returnVal
