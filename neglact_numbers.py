#input="is1 thi0s t3est 2a"
input="t2o j3oin 4wonderbiz i0 technolog5ies wan1t"
list1=input.split(" ")
numbers='0123456789'
output=[]
for i in list1:
    for j in i:
        if j in numbers:
            pos=int(j)
            output.insert(pos,i)

final=''
for o in output:
    final=final+o+" "

for l in final:
    if l not in numbers:
        print(l,end="")
        
