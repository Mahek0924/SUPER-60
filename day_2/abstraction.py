# #by default we cant use abstraction in python so we use abc module
# from abc import ABC, abstractmethod
# class Company(ABC):  #abstract class
#     @abstractmethod   #decorator
#     def training(self):    #abstract method
#         pass

#     @abstractmethod   #decorator
#     def placement(self):    #abstract method
#         pass

# class Aadvik(Company):
#     def training(self):    #abstract method implementation
#         print("C, C++, Java")
#     def placement(self):    #abstract method implementation
#         print("Java Placement")

# class Litesh(Company):
#     def training(self):    #abstract method implementation
#         print("Python, Django")
#     def placement(self):    #abstract method implementation
#         print("Python Placement")

# class BKPatil(Company):
#     def training(self):    #abstract method implementation
#         print("Machine Learning")
#     def placement(self):    #abstract method implementation
#         print("Data Science Placement")

# obj1 = Aadvik()
# obj1.training()
# obj1.placement()

# obj2 = Litesh()
# obj2.training()
# obj2.placement()

# obj3 = BKPatil()
# obj3.training()
# obj3.placement()






#===============================================================



from abc import ABC, abstractmethod
class Irctc(ABC):  #abstract class
    @abstractmethod   #decorator
    def bookTicket(self):    #abstract method
        pass

class MakeMyTrip(Irctc):
    def bookTicket(self):    #abstract method implementation
        print("==============================")
        print("  Welcome to makemyterip.com  ")
        source = input("Enter source station: ")
        destination = input("Enter source destination: ")
        date = input("Enter date: ")
        print("==============================")

class Goibibo(Irctc):
    def bookTicket(self):    #abstract method implementation
        print("    G  O  I  B  I  B  O   ")
        print("  Welcome to goibibo.com  ")

class Yatra(Irctc):
    def bookTicket(self):    #abstract method implementation
        print("  Welcome to yatra.com  ")

obj1 = MakeMyTrip()
obj1.bookTicket()

obj2 = Goibibo()
obj2.bookTicket()

obj3 = Yatra()
obj3.bookTicket()
