#reverse a string using stack individually
#example -input=Python programming language
#output=nohtyP gnimmargorp egaugnal
#eg -false = egaugnal gnimmargorp nohtyP

string="Python programming language"
word=string.split(" ")
length=len(word)
double_length=2*length
i=0
while(length < double_length):
    if i%2 !=0:
        word.insert(i," ")
        length+=1
    i+=1
for i in range(0,len(word)):
    for j in range(0,len(word[i])):
        word.append(word[i][j])

    for k in range(-1,-len(word[i])-1,-1):
        print(word[i][k], end="")
