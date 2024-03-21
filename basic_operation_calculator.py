import sys
def add(first_number,second_number):

    return int(first_number)+int(second_number)

def sub(first_number,second_number):
    return int(first_number)-int(second_number)

def mul(first_number,second_number):
    return int(first_number)*int(second_number)

def div(first_number,second_number):
    return int(first_number)/int(second_number)

def mod(first_number,second_number):
    return int(first_number)%int(second_number)

def floor_division(first_number,second_number):
    return int(first_number)//int(second_number)


def user_choice():
    print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.division \n 5.modularation \n 6.Floor division \n ")
    choice=int(input("enter your choice : "))
    operations(choice)

def operations(choice):
    if choice==1:
        first_number=input("enter a 1st number")
        second_number=input("enter a 2nd number")
        answer=add(first_number,second_number)

        print(f"{first_number} + {second_number} = {answer}")
        option=input("Do you want calculator for another operation? y/n : ")
        if option.lower()=='y':
            user_choice()
        else:
            sys.exit(0)
    if choice==2:
        first_number=input("enter a 1st number")
        second_number=input("enter a 2nd number")
        answer=sub(first_number,second_number)
        print(f"{first_number} - {second_number} = {answer}")
        option=input("Do you want calculator for another operation? y/n")
        if option.lower()=='y':
            user_choice()
        else:
            sys.exit(0)        
    if choice==3:
        first_number=input("enter a 1st number")
        second_number=input("enter a 2nd number")
        answer=mul(first_number,second_number)
        print(f"{first_number} * {second_number} = {answer}")
        option=input("Do you want calculator for another operation? y/n")
        if option.lower()=='y':
            user_choice()
        else:
            sys.exit(0)
    if choice==4:
        first_number=input("enter a 1st number")
        second_number=input("enter a 2nd number")
        answer=div(first_number,second_number)
        print(f"{first_number} / {second_number} = {answer}")
        option=input("Do you want calculator for another operation? y/n")
        if option.lower()=='y':
            user_choice()
        else:
            sys.exit(0)     
    if choice==5:
        first_number=input("enter a 1st number")
        second_number=input("enter a 2nd number")
        answer=mod(first_number,second_number)
        print(f"{first_number} % {second_number} = {answer}")
        option=input("Do you want calculator for another operation? y/n")
        if option.lower()=='y':
            user_choice()
        else:
            sys.exit(0) 
    if choice==6:
        first_number=input("enter a 1st number")
        second_number=input("enter a 2nd number")
        answer=floor_division(first_number,second_number)
        print(f"{first_number} // {second_number} = {answer}")
        option=input("Do you want calculator for another operation? y/n")
        if option.lower()=='y':
            user_choice()
        else:
            sys.exit(0)                        

user_choice()
