intGettheTotal = int(input())
intTotal = 0
i = 0
while intTotal <= intGettheTotal:
    intTotal = intTotal + int(input())
    if intTotal <= intGettheTotal:
        i = i + 1
print(i)
