intGettheTotal = int(input())
intList = []
intTotalList = []
intTotal = 0
strSet = 0
for i in range(0,4):
    intRawInput = input()
    if len(intRawInput) == 0 or (intRawInput.isnumeric() == False):
        intList.append(int(0))
        intTotalList.append(int(intTotal))
    else:
        intList.append(int(intRawInput))
        intTotal = int(intTotal) + int(intRawInput)
        intTotalList.append(int(intTotal))

    if intTotalList[i] < intGettheTotal:
        strSet = int(i) + 1
    elif intTotalList[i] == intGettheTotal:
        strSet = int(i) + 1
        print(strSet)
        quit()
    elif intTotalList[i] > intGettheTotal:
        print(strSet)
        quit()

print(strSet)
