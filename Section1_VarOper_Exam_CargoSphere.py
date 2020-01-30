import math
#Get the input from Users
intLenofCub = int(input())
intDiameterofCub = int(input())
intVolumeconsumped = int(input())
TotalVolumeofcub = intLenofCub * intLenofCub * intLenofCub
#print(TotalVolumeofcub)
Radiusofcub = (intDiameterofCub/2)
#print(Radiusofcub)
Volumeofsphere = (4/3) * 3.14 * (Radiusofcub ** 3)
#print(Volumeofsphere)
TotalVolumeofSphere = Volumeofsphere * intVolumeconsumped
RemainingVolumeofSphere = TotalVolumeofcub - TotalVolumeofSphere
print("%.2f" % round(RemainingVolumeofSphere,3))