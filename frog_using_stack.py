
stack=[]
frogs=[1,3,1,4,5,3,4]

stack.append(frogs[0])

for i in range(1,len(frogs)):
    if stack[-1] <= frogs[i]:
        stack.pop(-1)
        stack.append(frogs[i])
    else:
        stack.pop(-1)
        stack.append(frogs[i])    
    
print(stack)