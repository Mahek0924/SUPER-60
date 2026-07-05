#overloading  - python does not support method and constructor overloading

# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

#it does not work beacuse it only considers last method, so it gives error

#it supports operator overloading but not directly, it does indirectly




#---------------------------------------------------------------


#overriding

class Rbi:
    def homeloan(self):
        print("Home loan interest 8%")
    def carloan(self):
        print("Car loan interest 7%")

class SBI(Rbi):      #childclass
    def homeloan(self):
        print("Home loan interest 10.5%")
        super().homeloan()

sbiobj = SBI()
sbiobj.homeloan()