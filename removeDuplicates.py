str=input("enter the string")
removeDuplicates=""
for i in str:
    if i in removeDuplicates:
        continue
    else:
        removeDuplicates+=i 
print(removeDuplicates)        
