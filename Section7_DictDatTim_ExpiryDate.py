from datetime import datetime, timedelta

dtInputExp = datetime.strptime(input(),'%b %d %Y')
dtInputDep   = datetime.strptime(input(),'%b %d %Y')
dtDays = int(input())
dtCalcDate = dtInputDep + timedelta(days= dtDays)

if (dtCalcDate < dtInputExp):
    print("Yes")
else:
    print("No")


