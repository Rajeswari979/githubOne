#input="HELLO AND (WELCOME(TO THE)TCEA(CONTEST)TODAY)IS (SATURDAY())"
input="(9*(7-2)*(1*5)"
stack=[]
for i in input:
    if i == "(":
        stack.append(i)
    elif i == ")":
        stack.pop()

if len(stack)==0:
    print("0")
else:
    print("1")