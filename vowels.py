vowels="aeiou"
input='compuuter'
g=[]
previous=input[0]
for i in range(1,len(input)):
    if input[i] in vowels:
        if input[i] == previous:
            print(input[i])
            previous=input[i]
        else:
            print(input[i])
            previous=input[i]
        

