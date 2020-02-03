print("Enter the Numbers in List-1")
strInputOne = input()
print("Enter the Numbers in List-2")
strInputTwo = input()
intListOne = [int(n) for n in strInputOne.split()]
intListTwo = [int(n) for n in strInputTwo.split()]
intResulOutput = []
for intOne in intListOne:
    for intTwo in intListTwo:
        intResult = intOne * intTwo
        if (intResult % 2 != 0):
            intResulOutput.append(intResult)
if len(intResulOutput) > 0:
    print(*intResulOutput)
else:
    print("No such Elements in the list")

