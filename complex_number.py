class Complex_number:

    def details(self):
        real1=int(input("Enter real number of 1st complex number : "))
        real2=int(input("Enter real number of 2nd complex number : "))
        imag1=int(input("Enter imaginary number of 1st complex number : "))
        imag2=int(input("Enter imaginary number of 2nd complex number : "))
        return real1,real2,imag1,imag2

    def real_addition(self,real1,real2,imag1,imag2):
        real_sum=real1+real2
        imag_sum=imag1+imag2
        print(f"\nSum of the complex number is {real_sum} + {imag_sum}i\n")

     
obj=Complex_number()
d1,d2,d3,d4=obj.details()
obj.real_addition(d1,d2,d3,d4)

