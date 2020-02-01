intInputValue = int(input())
if intInputValue >= 0 and intInputValue <=1000:
    print("Saver")
elif intInputValue >= 1001 and intInputValue <=10000:
    print("Economy")
elif intInputValue >=10001:
    print("Flexi")