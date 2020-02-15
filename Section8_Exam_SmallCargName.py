fn = open('text.txt', 'r')
intList = []
for line in fn:
    line = line.strip('\n')
    line = line.strip()
    intList.append(len(line))
intList.sort()
fn.close()
fn = open('text.txt', 'r')
for line in fn:
    line = line.strip('\n')
    line = line.strip()
    if (len(line) == intList[0]):
        print(line)
fn.close()
