#remove duplicate letters in the string in given sentence
#example input - hello ,output -helo
#example input=python is a programming language
#output -python is a progamin langue 

sentance=input("enter the string : ")
str=sentance.split(' ')
removeDuplicates=""
new_sentance=""
def func(word):
   removeDuplicates=""
   for letter in word:
      if letter in removeDuplicates:
          continue
      else:
         removeDuplicates+=letter
   new_sentance=removeDuplicates
   return new_sentance     
         
         

for word in str:
    result=func(word)
    print(result,end=' ')
       
