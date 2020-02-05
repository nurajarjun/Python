from datetime import datetime, timedelta
strTupValues = ()
strListValues = []
intValues = int(input())
for i in range(1,intValues + 1):
    strTempInput = input()
    strTupValues = tuple(x for x in strTempInput.split(","))
    strListValues.append(strTupValues)
dtSearch = datetime.strptime(input(), '%d-%m-%Y')
print(strListValues)
for i in strListValues:
    #print( datetime.strptime(i[1], '%m-%d-%Y'))
    if  (datetime.strptime(i[1], '%d-%m-%Y')) >= dtSearch:
        print(i[0])






