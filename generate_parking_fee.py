parking_time=0
for_1hour=100
increment=150
for_30min=75
final_fee=0

entry_time=float(input("Enter the entry time : "))
exit_time=float(input("Enter the exit time : "))

parking_time=exit_time-entry_time

if parking_time<=0.15:
    print("No need to pay")

elif parking_time == 1:
    final_fee+=for_1hour
    print(" Pay ",final_fee,"rupees")

elif parking_time >1:
    final_fee=+for_1hour
    
    parking_time-=1
    time=round(parking_time,2)
   
    while(time>0):
        if time >=1:
            final_fee+=increment
                 
        elif time>0 and time <1 :
            if time <= 0.30 :
                final_fee+=for_30min
            else:
                final_fee=final_fee+increment
        time-=1
print("final fee",final_fee)   
     
        
           
        
        
    

        

