class Student:    #first letter of class name capital > naming convention
    rollno = 101  #data member

    def msg(self):  #member function
        print("Hello")

obj = Student()  #object creation
print(obj.rollno)  #accessing data member
obj.msg()  #accessing member function
print(obj)
