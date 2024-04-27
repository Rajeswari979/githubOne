
def seperate_by_dot(number):
    length=len(number)
    d_length=2*length
    ip=''
    if length<=6:
        for i in range(0,length):
            if i%2 !=0:
                number.insert(i,".")
        return number
    


        


#address=["0000","10026710","100242200"]
#for number in address:
number=list(input("enter"))
result=seperate_by_dot(number)
print(result)