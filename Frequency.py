MyDict = { }

Str = input("Please enter a string : ")


for x in Str:
        if x in MyDict:
            MyDict[x] += 1
        else:
            MyDict[x] = 1

des_dict = dict(sorted(MyDict.items(), key = lambda item: item[1], reverse = True))
print(des_dict)   
    
