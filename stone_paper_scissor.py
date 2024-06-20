import random
import sys
import tkinter

def get_choices():
    user_score=0
    computer_score=0
    while True:
        m=tkinter.Tk()
        print("-------------------------------------------------------------------")
        print("\t\tChoo se your option \n\t\t\t1.Rock\n\t\t\t2.Paper\n\t\t\t3.Scissor")
        print("-------------------------------------------------------------------")
        user_input=input("Enter Your Choice : ").lower()
        computer_chioce=random.choice(items)
        print("-------------------------------------------------------------------")
        print(f"\t\tYour Choice is : {user_input.capitalize()}\n\t\tComputer Choice is : {computer_chioce.capitalize()}")
       
        winner=determine_winner(user_input,computer_chioce)
        if winner =="user":
            user_score+=1
            print(f"\n\t<<<<<<<<<<<  Winner is {winner}  >>>>>>>>>>>")
        else:
            computer_score+=1
            print(f"\n\t<<<<<<<<<<<  Winner is {winner}  >>>>>>>>>>>")

        print(f"\n\t\tYour score is {user_score}\n\t\tComputer score is {computer_score} ")
        print("-------------------------------------------------------------------")

        print("Do you want to continue? yes=Enter 1 No=Enter 0")
        choice=int(input())
        if choice ==1:
            pass
        elif choice==0:
            sys.exit()
        else:
            print("Enter '1' for continue or Enter '0' for Quit")

def determine_winner(user_input,computer_chioce):
    if user_input in items:
            if user_input == computer_chioce:
                print(f"<<<<<<<<<<<   It's Tie   >>>>>>>>>>>")
            elif(user_input=="rock" and computer_chioce =="scissor")or(user_input=="paper" and computer_chioce =="rock")or(user_input=="scissor" and computer_chioce =="paper"):
                return "user"
            else:
                return "computer"
    else:
        print("Sorry....!, Your Choice is invalid")
        sys.exit()
    

items=["rock","paper","scissor"]
get_choices()


