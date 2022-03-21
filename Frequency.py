MyDict = { }

Str = input("Please enter a string : ")


for x in Str:
        if x in MyDict:
            MyDict[x] += 1
        else:
            MyDict[x] = 1

print(MyDict)   
    
