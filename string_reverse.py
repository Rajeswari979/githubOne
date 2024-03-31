#Reverse a string using stack
#eg: input=Hello
#output=olleH

string="Hello rajeswari madurai"
word=[]
for i in string:
    word.append(i)

for j in range(-1,-len(word)-1,-1):
    print(word[j],end=" ")    
