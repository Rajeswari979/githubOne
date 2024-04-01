list1=[1,2,5,4,3,8,2]
output=[]
for i in range(0,len(list1)-1):
    if list1[i] < list1[i+1]:
        list1[i]="e"
c=len(list1)
for i in range(0,c):
    if list1[i] == "e":
        list1.remove(list1[i])
        c-=1
print(list1) 

        
