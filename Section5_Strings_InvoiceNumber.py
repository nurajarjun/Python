strList= str(input())
strTempOne = ""
strTemptwo = ""
strTempSpecial = ""
strTempNumTwo = ""
strTempNumOne = ""
strTempAlphaTwo = ""
i = 1
if (strList[:1].isalpha()):
    for strchar in strList:
        if strTempNumOne == "Y":
            if (strchar.isalpha()):
                strTempAlphaTwo = "Y"
                if (strTempNumTwo != "Y"):
                    strTemptwo = strTemptwo + strchar
            elif (strchar.isnumeric()):
                if (strTempAlphaTwo == "Y"):
                    strTempNumTwo = "Y"
            else:
                strTempSpecial = "Y"
        else:
            if (strchar.isalpha()):
                strTempOne = strTempOne + strchar
            elif (strchar.isnumeric()):
                strTempNumOne = "Y"
            else:
                strTempSpecial = "Y"
            i = i + 1
else:
    print("Invalid Input")

if (strTempSpecial == "Y"):
    print("Invalid Input")
elif (strTempNumOne == "Y") and (strTempAlphaTwo == "Y" and strTempNumTwo == "Y"):
    print (strTempOne + " to " + strTemptwo)
else:
    print("Invalid Input")

