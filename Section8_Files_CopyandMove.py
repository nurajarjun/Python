fn = open('file_in.txt', 'r')
fn1 = open('file_out.txt', 'w')
for line in fn:
    fn1.write(line)
fn1.close()
fn.close()
fn2 = open('file_out.txt', 'r')
cont1 = fn2.read()
print(cont1)
