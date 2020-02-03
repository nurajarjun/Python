print("Enter the Numbers in List")
strInputOne = input()
test_list = []
intList = strInputOne.split()
print("Before Rotating :")
print(*intList)
test_list = intList[1:] +  intList[:1]
print("After Rotating : ")
print(*test_list)
