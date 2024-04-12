#check whether the given string is valid or not
#example input=278.98.0.2
#output invalid 
#input = 123.32.1.2
#output = valid

string=input("enter the address to check whether it is valid or not : ")
count=0
character=string.split('.')
if len(character)==4:
    for number in character:
        if int(number) <255 and int(number)>=0:
            count+=1
else:
    print("The given IP address is invalid")

if count ==4:
    print("The given IP address is valid")
else:
    print("The given IP address is invalid")    

    