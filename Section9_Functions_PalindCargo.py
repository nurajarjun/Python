def checkPalindrome(x):
    #remove spaces and special characters
    tempStrVar = ''.join(e.lower() for e in x if e.isalpha())
    strReversed = tempStrVar[::-1]
    if (tempStrVar == strReversed):
        return("Yes")
    else:
        return("NO")


mytxt = checkPalindrome(str(input()))
print(mytxt )
