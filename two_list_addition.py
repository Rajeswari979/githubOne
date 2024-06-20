
def operation(input_list):
    #reversed_list=input_list[::-1]
    string=''
    for num in input_list:
        string=str(num)+string
  
    return int(string)

first_number=operation([1,2,3])
second_number=operation([5,6,7])
addition=first_number+second_number
print(f"Answer is {addition}")
a=list(str(addition))
print(a[::-1])

 