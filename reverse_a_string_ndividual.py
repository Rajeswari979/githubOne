string="Hello World"
word=string.split(" ")

word.insert(1," ")
for i in range(0,len(word)):
    for j in range(0,len(word[i])):
        word.append(word[i][j])

    for k in range(-1,-len(word[i])-1,-1):
        print(word[i][k], end="")