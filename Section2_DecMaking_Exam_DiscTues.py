import math
#Get the input from Users
intTrainFare = int(input())
intTrainDuration = int(input())
intBusFare = int(input())
intBusDuration = int(input())
intFlightFare = int(input())
intFlightDuration = int(input())
intFare = int(input())
intDurWeight = int(input())

intCalTrain = (intTrainFare * intFare) + (intTrainDuration * intDurWeight)
intCalBus = (intBusFare * intFare) + (intBusDuration * intDurWeight)
intCalFlight = (intFlightFare * intFare) + (intFlightDuration * intDurWeight)
if (intCalTrain <  intCalBus) and (intCalTrain < intCalFlight):
    print("Train Transportation")
elif (intCalBus <  intCalTrain) and (intCalBus < intCalFlight):
    print("Bus Transportation")
elif (intCalFlight <  intCalBus) and (intCalFlight < intCalTrain):
    print("Flight Transportation")
