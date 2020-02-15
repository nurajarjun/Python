import xml.etree.ElementTree as ET
def cust_sort(t):
    return t[1]

tree = ET.parse('candidate.xml')
root = tree.getroot()
strList = []
strTupValues = ()
strCandidateName = ""
strAge = ""
for att in root.findall('candidate'):
    for a in att:
        if a.tag == "candidateName":
            strCandidateName = a.text
        elif a.tag == "age":
            strAge = a.text
    strTupValues = (strCandidateName, int(strAge))
    strList.append(strTupValues)
    strCandidateName = ""
    strAge = ""
for eachitem in strList:
    if eachitem[1] > 24:
        print(eachitem[0] + " : " + str(eachitem[1]))
