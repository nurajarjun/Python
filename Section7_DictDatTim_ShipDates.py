from datetime import datetime, timedelta
intListnums = [int(6), int(7)]
strstrNumDay = 0
dtInputDay = str(input())
dtInputCountdays = int(input())
dtInputExp = datetime.strptime(input(),'%d-%m-%Y')
i = 1
while i < dtInputCountdays:
    dtInputExp = dtInputExp + timedelta(days= 1)
    strNumDay = dtInputExp.isoweekday()
    if strNumDay not in intListnums:
        print(dtInputExp.strftime('%d-%m-%Y'))
        i = i + 1
