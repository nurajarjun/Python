import SeasonItemPrice
ses = SeasonItemPrice.SeasonItemPrice()
print("1) Price of item season-wise \n2) Seasonal Items")

intInput = int(input("Enter your choice"))

if intInput == 1:
    strInputitem = str(input("Enter the item name:"))
    strSeaonalList = ses.priceOfItemSeasonWise("item.xml", "season.xml", "SeasonItemPrice.xml", strInputitem)
    if len(strSeaonalList) > 0:
        print("Price of the item season-wise is")
        print('\n'.join(strSeaonalList))
    else:
        print("Item not found")
elif intInput == 2:
    strInputitem = str(input("Enter the item name:"))
    strseasonalname = ses.seasonalItem("item.xml", "season.xml", "SeasonItemPrice.xml", "Winter")
    if len(strseasonalname) > 0:
        print("Price of the item season-wise is")
        print('\n'.join(strseasonalname))
    else:
        print("No Seasonal Item for this month")
else:
    print("Invalid choice")




