i=0

rows,cols=5,5

parking_lot=[[0 for i in range(rows)] for i in range(cols)]
print(parking_lot)

def parking(choice):
    if choice.lower()=="y":
       for row in range(0,rows):
           for col in range(0,cols):
               if parking_lot[row][col] == 0:
                   parking_lot[row][col]="booked"
                   i+=1
                   return f"slot number {i} is allocated for you"
    elif choice == "1":
        print(parking_lot)
    else:
        print("sorry")
  
        
while(True):
      choice=input("Are you park here? Y/N \n Press 1 for slot")
      result=parking(choice)
      print(result)
            
