class Base:
    def __init__(self):
        print("Parentclass constructor called")
        self.a = "mahek"   #public data member
        self.__c = "pranav"   #private data member

#creating derived / child class
class Derived(Base):
    def __init__(self):
        #calling constructor of base class
        Base.__init__(self)
        # print("Calling private member of base class")
        # print(self.a)
        # print(self.__c)

# obj1 = Derived()
# print(obj1.a)
# print(obj1.__c)
obj2 = Base()
print(obj2.a)  # accessible
print(obj2.__c)   # not accessible