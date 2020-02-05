intTupValues = ()
intResultTuples = ()
strInputValues = input()
intTupValues = tuple(int(x) for x in strInputValues.split(',') )
intList = list(intTupValues)
#print(intList)
strnewList = []
[strnewList.append(x) for x in intList if x not in strnewList]
#print(strnewList)
intResultTuples = tuple(strnewList)
print(intResultTuples)
