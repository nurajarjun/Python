intinputValue = str(input())
intinputmaxValue = int(input())
intList = [int(n) for n in intinputValue.split(',')]
newList = []
newList = sorted(intList,reverse = True)
print(sum(newList[0:intinputmaxValue]))
