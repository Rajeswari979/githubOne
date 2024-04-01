#Input : [1,2,5,4,3,2,2]
#Output : [5,4,3,2,2]
#Explanation : Frog (1) ate Frog(0); Frog(2) ate Frog (1). Rest of the frogs are alive
#Input : [4,3,3,2,1]
#Output : [4,3,3,2,1]

def find_alive_frogs(frogs):
    frogs.append(0)
    alive_frogs=[]

    for i in range(0,len(frogs)-1):
        if frogs[i] < frogs[i+1]:
            pass
        else:
       
           alive_frogs.append(frogs[i])
    return alive_frogs       

print("Alive frogs = ",find_alive_frogs([1,2,5,4,3,2,2]))
print("Alive frogs = ",find_alive_frogs([4,3,3,2,1]))

        
