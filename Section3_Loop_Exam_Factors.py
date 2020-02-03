intInput = int(input())
strText = ""
for i in range(1, intInput + 1):
    if intInput % i == 0:
        strText = strText + str(i) + " "
print(strText)
