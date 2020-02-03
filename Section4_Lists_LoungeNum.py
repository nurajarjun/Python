strList= []
strinputValue = str(input())
strSearch = (input())
strList = (strinputValue.split(","))
try:
    strList.index(strSearch)
    res_list = c
    print(*res_list, sep = "\n")
except:
    print(0)

