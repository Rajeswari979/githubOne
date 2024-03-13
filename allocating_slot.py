def allocate():
    global i
    for row in range(0,rows):
        for col in range(0,cols):
            if parking_lot[row][col] == 0:
                parking_lot[row][col]="booked"
                i+=1
                id=i
                return f"Slot Number {i} is allocated for you"
 
def select(select_row , select_col):
    global i
    if parking_lot[select_row][select_col] == 0:
        parking_lot[select_row][select_col]="booked"
        
         
rows,cols=5,5
i=0
parking_lot=[[0 for i in range(rows)] for i in range(cols)]
print(parking_lot)

while(True):
    choice=input("Are you park here? Y/N : ")
    if choice.lower()=="y":
       name=input("Enter your name : ")
       city=input("Enter your city : ")
       print("*****SELECT YOUR CHOICE***** \n\n 1.Allocate me a slot \n 2.I want to select a slot ")
       option=int(input())
       if option == 1:
           print(allocate())
           
       elif option == 2:
           print("Available slots")
           print(parking_lot)
           select_row = int(input("select your row to park : "))
           select_col = int(input("select your col to park : "))
           select(select_row , select_col)
           
                        
    elif choice.lower()== "n":
        print("Thank You......")
  
