print("Enter the type of relationship with customer")
#print("")
strCustType = input().upper()
#print(strCustType)
print("Enter the slot of the customer")
#print("")
strCustSlot = input().upper()
#print(strCustSlot)
if strCustType == "NEW":
    intType = 10
elif strCustType == "GOLD":
    intType = 25
elif strCustType == "PLATINUM":
    intType = 40
else:
    print("Invalid Input")
    quit()


if strCustSlot == "S1":
    intAmount = 200
elif strCustSlot == "S2":
    intAmount = 800
elif strCustSlot == "S3":
    intAmount = 200
elif strCustSlot == "S4":
    intAmount = 800
else:
    print("Invalid Input")
    quit()
intCalc = int(intAmount - ((int(intType) * int(intAmount))/100))
print("Amount to be paid = " + str(intCalc))