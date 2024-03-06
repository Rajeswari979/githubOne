#get a name from user
name = input("enter the name : ")

#using 2 forloop for develop pyramid
#outer for loop for iterate name's length
for i in range(0,len(name)):
    #inner forloop for displaying character like a pyramid
    for j in range(0,i+1):
        #using end=" " for avoid new line and display the character
        print(name[j] , end=" ")
    
    print("\r")
