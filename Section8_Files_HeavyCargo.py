import operator
def cust_sort(t):
    return t[1]
intInputVal = int(input("Enter the n value \n"))
fn = open('readlines.txt', 'r')
strList = []
strListTwo = []
strListThree = []
strTupValues = ()
for line in fn:
    line = line.strip('\n')
    line = line.strip()
    line = line.replace(" ","")
    strListTwo = line.split("-")
    #print(strListTwo[0])
    strTupValues = (strListTwo[0], int(strListTwo[1]))
    strList.append(strTupValues)
fn.close()
strList.sort(key=lambda x: x[1],reverse=True)
for i in range(0,intInputVal):
    strListThree.append(strList[i][0] + " - " + str(strList[i][1]))

strListThree.reverse()
for strVals in strListThree:
    print(strVals)
