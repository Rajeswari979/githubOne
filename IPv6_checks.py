'''
input :
ip_address="ab13:2fd:67ce:0000:ffab:7896:FFFF:1235"
output :
valid or invalid

'''


import sys

ip_address="ab13:2fd:67ce:0000:ffab:7896:FFFF:1235"
address=ip_address.lower()
octets=address.split(':')
if len(octets) !=8:
    print("inValid length")
    sys.exit()

for octet in octets:
    if len(octet)<=4:
        pass
    else:
        print("inValid length")
        sys.exit()

for number in octets:
    for i in range(len(number)):
        if (ord(number[i]) <= 57 and ord(number[i])>=48) or (ord(number[i])>=97 and ord(number[i])<=102 ):
            pass
        else:
            print(f"{address} is inValid IP address")
            sys.exit()

print(f"The Given Address is Valid IP address")