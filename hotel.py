import sys
menu=["idly","dosa","poori","vadai","pongal","parota","idiyapam","masala dosa","chicken biriyani","chicken gravy"]
price=[15,35,25,10,50,20,25,60,180,150]
amount=0
totalAmount=0
while(True):
  print("\n1.add a item on menu(admin only can access)\n2.print the menu\n3.calculate the bill\n4.close\nEnter your option : ")
  option=int(input())
  if option==1:
    password=input("enter you passcode : ")
    if password == "Rajeswari":
      newDish=input("Add a dish in menu : ")
      menu[-1]=newDish
      if newDish in menu:
        print("Sorry, item is already in menu")
      else:
        newDishprice=int(input("Enter the price of the dish : "))
        price[-1]=newDishprice
    else:
       print("Ooops, its wrong")    

  elif option==2:
    print("*****MENU*****")
    for i in range (0,len(menu)):
       print(i+1,")",menu[i],"--",price[i])
  elif option==3:
    choice=input("Are you Ready? y/n : ")
    while choice.lower()=="y": 
      dish=input("Enter a dish : ")
      quantity=int(input("Enter the quantity : "))
      for i in range(0,len(menu)):
          if menu[i]==dish:
             amount=price[i]*quantity
      
             totalAmount += amount       
      
      choice=input("Do you want to add a dish? y/n : ")
    print("Bill Amount :",totalAmount) 

    print("Do you have coupon code for discount? y/n : ")
    couponChoice=input()
    if couponChoice=="y":
      couponCode=int(input("Enter the coupon code : "))
      if couponCode==880:
          discount=totalAmount*(10/100)
          finalAmount=totalAmount-discount
      print("Your Final Bill Amount is ",finalAmount)

    elif option==4:
         print("THANKS FOR VISITING......")
         sys.exit(0)  



