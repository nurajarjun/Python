def customized(str):
    strcustomList = []
    strcustomList = tuple(x.split(" ") for x in str.split(","))
    return strcustomList

def convert(custom, original):
    strOutputResult = ""
    strNoOutput = False
    for eachWord in original.split(" "):
        if eachWord in custom:
            strOutputResult = strOutputResult + " " + custom[eachWord]
        else:
            strNoOutput = True
    if strNoOutput:
        return "The sentence cannot be translated"
    else:
        return strOutputResult.strip()

def checkthestringvalidity(strForeign, strStored):
    intSplitcount = len(strForeign.split(","))
    intSplitstorecount = len(strStored.split(" "))
    if intSplitstorecount > intSplitcount:
        return False
        print ("False")
    else:
        return True
        print("True")


strinput = str(input())
strSentinput = str(input())
if checkthestringvalidity(strinput,strSentinput):
    strtupupdated = dict(customized(strinput))
    print (convert(strtupupdated,strSentinput ))
else:
    print("The sentence cannot be translated")
