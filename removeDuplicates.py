sentance=input("enter the string : ")
removeDuplicates=""

for letter in sentance:
    if letter in removeDuplicates:
        continue
    else:
        removeDuplicates += letter

print("final string : ",removeDuplicates)

