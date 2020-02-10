import xml.etree.ElementTree as ET
import csv
tree = ET.parse('product.xml')
root = tree.getroot()
f = open('product.csv','w', newline='')
csvwriter = csv.writer(f)
head = ['id', 'productName','cost','weight']
csvwriter.writerow(head)
for att in root.findall('product'):
    row = []
    for a in att:
        second = a.text
        row.append(second)
    csvwriter.writerow(row)
f.close()
fn = open('product.csv', 'r')
for line in fn:
    line = line.strip('\n')
    line = line.strip()
    line = line.replace(" ","")
    print(line)
