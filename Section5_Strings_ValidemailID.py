import string
strInpemail = input()
strRule3 = strInpemail.split("@")[0]
strTemp = strInpemail.split("@")[1]
strRule2 = strTemp.split(".")[0]
strRule1 = strTemp.split(".")[1]
strSpecialCharacters = ['@','!','#','$','%','^','&','*','(',')','<','>','?','/','|','}','{','~',':',']','[', ' , ', ' \ ', " ' "]

if (strRule1 == "com") or (strRule1 == "in") or (strRule1 == "edu"):
    RuleOne = "TRUE"
else:
    RuleOne = "FALSE"

if len(strRule2) > 3:
    RuleTwo = "TRUE"
else:
    RuleTwo = "FALSE"

if (strRule3.islower()):
    if (strRule3[:1]).isalnum() and (strRule3[len(strRule3) - 1:]).isalnum():
        strList = list(strchar for strchar in strRule3 if strchar in strSpecialCharacters)
        if len(strList) == 0:
            RuleThree = "TRUE"
        else:
            RuleThree = "FALSE"
    else:
        RuleThree = "FALSE"
else:
    RuleThree = "FALSE"

if (RuleOne == "FALSE") or (RuleTwo == "FALSE") or (RuleThree == "FALSE"):
    print("Invalid")
    if RuleOne == "FALSE":
        print("1")
    if RuleTwo == "FALSE":
        print("2")
    if RuleThree == "FALSE":
        print("3")

else:
    print("Valid")
