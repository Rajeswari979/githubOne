
def func(count,a):
    for i in range(count):
        name=input("enter name : ")
        python_marks=int(input("enter marks : "))
        a[name]=python_marks
    return a

dic_1={}
a={}
dic_2={}
dic_3={}

no_of_stud1,no_of_stud2,no_of_stud3=input("enter no of students in each dept : ").split(",")
result1=func(int(no_of_stud1),dic_1)
result2=func(int(no_of_stud2),dic_2)
result3=func(int(no_of_stud3),dic_3)

for i,k in result1.items():
    print(i,k)
for i,k in result2.items():
    print(i,k)
for i,k in result3.items():
    print(i,k)        

marks_sort1=sorted(result1.values(),reverse=True)    
top3_in_1=marks_sort1[0:3]
print(top3_in_1)

marks_sort2=sorted(result2.values(),reverse=True)    
top3_in_2=marks_sort2[0:3]
print(top3_in_2)
 
marks_sort3=sorted(result3.values(),reverse=True)    
top3_in_3=marks_sort3[0:3]
print(top3_in_3)

all_marks=top3_in_1+top3_in_2+top3_in_3

top3_among_all=sorted(all_marks,reverse=True)
print(f"{top3_among_all[0:3]} toppers among all three class")

#names
value={i for i in result1 if result1[i]==300 }
print(value)