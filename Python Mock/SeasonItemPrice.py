import xml.etree.ElementTree as ET
class SeasonItemPrice:
    def priceOfItemSeasonWise(self,itemFile,seasonFile,seasonItemPriceFile,itemName):
        intitemNumber = 0
        strItemName = ""
        strcategory = ""
        strSeason = []
        strSeasonItem = []
        strfinaloutput = []

        tree = ET.parse(itemFile)
        root = tree.getroot()
        for att in root.findall('Item'):
            if (att.find('itemName').text == itemName):
                strItemName = att.find('itemName').text
                intitemNumber = int(att.find('itemNumber').text)
                strcategory = att.find('category').text

        tree = ET.parse(seasonFile)
        root = tree.getroot()
        for att in root.findall('Season'):
                templist = []
                intseasonNumber = int(att.find('seasonNumber').text)
                templist.append(intseasonNumber)
                strseasonName = att.find('seasonName').text
                templist.append(strseasonName)
                strdescription = att.find('description').text
                templist.append(strdescription)
                strSeason.append(templist)

        tree = ET.parse(seasonItemPriceFile)
        root = tree.getroot()
        for att in root.findall('seasonItemPrice'):
            templist = []
            intSeasonNum = int(att.find('season').text)
            intItemNum   = int(att.find('item').text)
            intPriceVal  = int(att.find('price').text)
            if (intitemNumber == intItemNum):
                strSeasoninfo = ' '.join([eas[1] for eas in strSeason if eas[0] == intSeasonNum])
                templist.append(intSeasonNum)
                templist.append(intItemNum)
                templist.append(intPriceVal)
                strSeasonItem.append(templist)
                strfinaloutput.append(str(strSeasoninfo) + " - " + str(intPriceVal))

        return (strfinaloutput)

    def seasonalItem(self,itemFile,seasonFile,seasonItemPriceFile,seasonName):
        intSeasonNum = 0
        strSeasonitemlist = []
        stroutput = []
        tree = ET.parse(seasonFile)
        root = tree.getroot()
        for att in root.findall('Season'):
            if (att.find('seasonName').text == seasonName):
                intSeasonNum = int(att.find('seasonNumber').text)

        tree = ET.parse(seasonItemPriceFile)
        root = tree.getroot()
        for att in root.findall('seasonItemPrice'):
            if (int(att.find('season').text) == intSeasonNum):
                strSeasonitemlist.append(int(att.find('item').text))

        tree = ET.parse(itemFile)
        root = tree.getroot()
        for att in root.findall('Item'):
            if (int(att.find('itemNumber').text) in strSeasonitemlist):
                stroutput.append(att.find('itemName').text)

        return stroutput





