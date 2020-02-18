#check function to check the entire string by calling all functions
def check(inp):
    #for each cargo in string
    while(inp.find("{")!=-1):
                    start=inp.find("{")
                    end=inp.find("}",start)
                    print(start)
                    print(end)
                    substring=inp[start+1:end]
                    print(substring)
                    #checking each cargo
                    if(substring.find("}")!=-1 or end==-1 or checkCargo(substring)==False):
                                    return False
                    inp=inp[end+1:]
    #if string has an extra } symbol
    if(inp.find("}")!=-1):
                    return False
    return True
#Function for checking a Cargo
def checkCargo(inp):
                #check for a nested cargo
                if(inp.find("{")!=-1):
                                return False
                #for each container in string
                while(inp.find("[")!=-1):
                                start=inp.find("[")
                                end=inp.find("]",start)
                                substring=inp[start+1:end]
                                #checking each container
                                if(substring.find("]")!=-1 or end==-1 or checkContainer(substring)==False):
                                                return False
                                inp=inp[end+1:]
                #if string has an extra ] symbol
                if(inp.find("]")!=-1):
                                return False
                return True
#Function for checking a Container
def checkContainer(inp):
                #check for a nested container
                if(inp.find("[")!=-1):
                                return False
                #for each box in string
                while(inp.find("(")!=-1):
                                start=inp.find("(")
                                end=inp.find(")",start)
                                substring=inp[start+1:end]
                                #checking each box
                                if(substring.find(")")!=-1 or end==-1 or checkBox(substring)==False):
                                                return False
                                inp=inp[end+1:]
                #if string has an extra ) symbol
                if(inp.find(")")!=-1):
                                return False
                return True
#Function for checking a Box
def checkBox(inp):
                #checking the box
                if(inp.find("}")!=-1 or inp.find("{")!=-1 or inp.find("(")!=-1 or inp.find(")")!=-1 or inp.find("]")!=-1 or inp.find("[")!=-1):
                                return False
                else:
                                return True

def findtheoccurencesofcargo(inp):
    open = inp.count("{")
    close = inp.count("}")
    locofCargo = inp.find("{")
    locofBox = inp.find("(")
    locofContainer = inp.find("[")
    stropenclose = "Valid"
    strlocofCargo = "Valid"
    if open > 1 or close > 1:
        stropenclose = "not valid"
        print("1 " + stropenclose)

    if locofCargo > locofBox or locofCargo > locofContainer:
        strlocofCargo = "not valid"
        print(strlocofCargo)

    if stropenclose == "not valid" or strlocofCargo == "not valid":
        return False
    else:
        return True

strUserinput = str(input())
if findtheoccurencesofcargo(strUserinput):
    strinput = check(str(strUserinput))
    print('Valid' if strinput else 'Invalid' )
else:
    print("Invalid")
