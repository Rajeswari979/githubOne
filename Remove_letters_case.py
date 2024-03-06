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
   print("Letter are Removed : ",func(word.lower()))
 

    
       
