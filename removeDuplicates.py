sentance=input("enter the string : ")
removeDuplicates=""
str=sentance.split(' ')
print(str)

def removingCharacter(word1):
     removeDuplicates=""
     for i in word1:
        if i in removeDuplicates:
            continue
        else:
           removeDuplicates+=i 
        #print("Duplicates are removed - ",removeDuplicates)
        removed=removeDuplicates   
        return removed  

for word in str:
    print(removingCharacter(word),end=" ")


