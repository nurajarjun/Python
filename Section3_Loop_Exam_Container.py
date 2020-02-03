i=1
while True:
    temp = int(input("Enter the number of items in the box %d\n" % i))
    if temp%8 ==0:
        i+=1
    else:
        break
print("Number of boxes stored in container is %d" % (i-1))
