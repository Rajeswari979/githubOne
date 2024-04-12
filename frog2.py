f=[1,1,1,5]
c=len(f)+1
max=f[0]
i=1
while i!=c:
    if max<=f[i]:
        temp=max
        max=f[i]
        f.remove(temp)
        c=c-1
        i=i+1
    else:
        i=i+1
        
print (f)