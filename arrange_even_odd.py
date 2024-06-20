input=[1,2,3,5,4,7,10]
even=[]
odd=[]
for num in input:
    if num %2==0:
        even.append(num)
    else:
        odd.append(num)

sorted_odd=[]
sorted_odd.append(odd[0])
for i in range(1,len(odd)):
    if odd[i] < sorted_odd[0]:
        sorted_odd.insert(1,odd[i])
    else:
        sorted_odd.insert(len(odd),odd[i])

sorted_even=[]
sorted_even.append(even[0])
for ii in range(1,len(even)):
    if even[ii] < sorted_even[0]:
        sorted_even.insert(0,even[ii])
    else:
        sorted_even.insert(1,even[ii])


print(sorted_odd)
print(sorted_even)