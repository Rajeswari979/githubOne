'''
input :
ip_address="ab13:2fd:67ce:0000:ffab:7896:FFFF:1235"
output :
valid or invalid

'''
import sys
file=open("trial_read.txt","r")
ip_address=file.readline()
address=ip_address.lower()
hextet=address.split(':')
if len(hextet) !=8:
    print("inValid length")
    

for hextets in hextet:
    if len(hextets)<=4:
        pass
    else:
        print("inValid length1") 
        continue

for number in hextet:
    for i in range(len(number)):
        if (ord(number[i]) <= 57 and ord(number[i])>=48) or (ord(number[i])>=97 and ord(number[i])<=102 ):
            pass
        else:
            print(f"{address}\tis inValid IP address",)
            break

print(f"The Given Address is Valid IP address")