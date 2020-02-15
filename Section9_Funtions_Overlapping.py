def checkOverlap(x,y):
    count = 0
    for eachsub in x:
        if eachsub in y:
            count = count + 1

    if (count > 0):
        return("Overlapping")
    else:
        return("Non Overlapping")

def splittheInputstring(TempStr):
    strInput = []
    strCleanOutput = []
    strInput = TempStr.split(",")
    strCleanOutput = [eachItem.strip(' ').lower() for eachItem in strInput]
    return(strCleanOutput)

def splittheInputstringOriginal(TempStr):
    strInput = []
    strCleanOutput = []
    strInput = TempStr.split(",")
    strCleanOutput = [eachItem.strip(' ') for eachItem in strInput]
    return(strCleanOutput)

strInputOne = str(input())
strInputTwo = str(input())

print(splittheInputstringOriginal(strInputOne))
print(splittheInputstringOriginal(strInputTwo))
strResult = checkOverlap(splittheInputstring(strInputOne), splittheInputstring(strInputTwo))
print(strResult)
