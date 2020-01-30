import math
#Get the input from Users
intLenofCont = int(input())
intLenofCargo = int(input())
intFindLocation = int(input())
#Get the input from user ends here

#Get the count for cargo in a container
intgetthecountofcargo = intLenofCont/intLenofCargo
intTotalnumberofcargoincontainer = intgetthecountofcargo * intgetthecountofcargo
#print("Count of cargo " + str(intgetthecountofcargo))
#print("Total in a container " + str(intTotalnumberofcargoincontainer))

#Get the count of containers needed to optimize
intDivisor = intFindLocation/intTotalnumberofcargoincontainer
#print("Find nearest Divisor" + str(intDivisor))
intlocalValue = 0
if intDivisor.is_integer():
    #print("number is integer")
    intlocalValue = intDivisor - 1
else:
    #print("number is float")
    intlocalValue = math.trunc(intDivisor)
#print("Print the lowest divisor " + str(intlocalValue))

intArrayStart = (intlocalValue * intTotalnumberofcargoincontainer) + 1
#print("Array Start " + str(intArrayStart))
intcountofValues = ((intFindLocation - intArrayStart) + 1)
#print("Count of Values " + str(intcountofValues))
if (intcountofValues%intgetthecountofcargo!=0):
    intPosoflen = int((intcountofValues%intgetthecountofcargo) - 1)
else:
    intPosoflen = int((intgetthecountofcargo - 1))
#print("Position of length " + str(intPosoflen))
intPosofbreadth = math.ceil((intcountofValues/intgetthecountofcargo)) - 1
#print("Position of breadth " + str(intPosofbreadth))
#print("Position of Container " + str(intlocalValue))
print(str(intPosoflen),str(intPosofbreadth),str(intlocalValue))
