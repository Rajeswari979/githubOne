str=input("enter the sentance : ")
addSpace=""
for i in range(0,len(str)):
    if i % 2==0:
        addSpace+=" "+str[i]
    else:
        addSpace+=str[i]

print(addSpace)
