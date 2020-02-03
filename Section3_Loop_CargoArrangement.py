intGettheCount = int(input())
strStar = "*"
strAsh = "#"
StrPlus = "+"
intTempCountStart = intGettheCount - 1
intDeflength = int((intTempCountStart * 2) + 1)
for i in range(1,int(intGettheCount + 1)):
    intRemainingLength = intDeflength - (intTempCountStart * 2)
    print((strAsh * intTempCountStart) + (strStar * intRemainingLength) + (StrPlus * intTempCountStart))
    intTempCountStart = intTempCountStart - 1
