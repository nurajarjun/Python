intValOne = int(input())
intValTwo = int(input())
intValThree = int(input())
intValFour = int(input())
intValTotal = int(input())

if intValTotal <= intValOne:
    print("1")
elif intValTotal <= (intValOne + intValTwo):
    #print(intValOne + intValTwo)
    print("2")
elif intValTotal <= (intValOne + intValTwo + intValThree):
    print("3")
    #rint(intValOne + intValTwo + intValThree)
elif intValTotal <= (intValOne + intValTwo + intValThree + intValFour):
    print("4")
    #print(intValOne + intValTwo + intValThree + intValFour)
elif (intValOne + intValTwo + intValThree + intValFour) < intValTotal:
    print("Not Possible")