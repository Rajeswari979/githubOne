input=[1,2,3,3,3,4,4,7,7,9]
output_list=[]
count=0
previous=''

for element in input:
    if element==previous:
        count+=1
    else:
        output_list.append(element)  
        previous=element  

for i in range(count):
    output_list.append("_")

print(output_list)