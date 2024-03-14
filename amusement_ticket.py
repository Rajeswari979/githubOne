from datetime import date
from datetime import datetime

today=date.today()


#def get_details_from_user():
user_birthday=input("Please enter your birthday (YYYY-MM-DD): ")
birthday = datetime.strptime(user_birthday, "%Y-%m-%d").date()

#print(user_birthday.year)
print(today.year)
print(birthday.year)

age = today.year - birthday.year
print(age)
    
