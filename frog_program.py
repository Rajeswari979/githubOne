frogs=[1,2,5,4,3,2,2]
frogs.append(0)
alive=[]
for i in range(0,len(frogs)-1):
    if frogs[i] < frogs[i+1]:
        pass
    else:
       
        alive.append(frogs[i])

print(alive)

        
