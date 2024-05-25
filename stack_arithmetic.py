'''
input=["1","2","+","5","*"]
(1+2)*5=15
output =[15]
'''
def stack_implementation(input):
    for element in input:
        if element.isnumeric():
            stack.append(int(element))
        else:
            if len(stack)>=2: 
                b=stack.pop()
                a=stack.pop()

                if element == "+":
                    result=a+b
                    stack.append(result)
                elif element == "-":
                    result=a-b
                    stack.append(result)
                elif element == "*":
                    result=a*b
                    stack.append(result)
                elif element == "/":
                    result=a/b
                    stack.append(result)
                elif element == "%":
                    result=a%b
                    stack.append(result)
                else:
                    print("This operator doesnt specified")
            else:
                print("Your stack doesnt have enough elements......!")
    
    return stack

#input=["10","2","3","+","-","5","*"]
input=["1","2","+","5","*"]
stack=[] 
print(stack_implementation(input))
