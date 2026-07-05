# class Demo:
#     def __init__(self):
#         print("I am constructor and i am always called first")

#     #method
#     def info(self):
#         print("I am a method")

# obj = Demo()  #object creation  #for 1 object only once a constrcutor is called, automatically called when object is created
# obj.info()  #calling the method
# obj2 = Demo()  #for 2nd object constructor is called again


# class Hod:
#     def __init__(self):
#         self.name = "mahek"      #2 byte
#         self.age=20              #3 byte
#         self.stid=101            #1 byte
#     def info(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Student id:",self.stid)
# obj = Hod()  #object creation
# obj.info()



# class Hod:
#     def __init__(self,name,age,stid):
#         self.name = name      #2 byte
#         self.age=age              #3 byte
#         self.stid=stid            #1 byte
#     def show(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Student id:",self.stid)
# obj = Hod("mahek",20,101)  #object creation with postional arguments
# obj.show()


# #instance variable
# class New:
#     def __init__(self):
#         self.a=10
# obj1= New()
# obj2= New()
# obj3= New()
# obj1.a=20
# print(obj1.a)  #20  
# print(obj2.a)  #10
# print(obj3.a)  #10




# #static variable
# class New:
#     a=10
#     def __init__(self):
#         self.name="mahek" 

# obj1= New()
# obj2= New()
# obj3= New()
# New.a=20
# print(obj1.a)  #20
# print(obj2.a)  #20
# print(obj3.a)  #20



# class College:
#     collegename="MIT"  #static variable
#     def __init__(self):
#         self.name="mahek"  #instance variable
# s1=College()
# s2=College()
# s3=College()
# print("s1=",s1.collegename,"...",s1.name)
# print("s2=",s2.collegename,"...",s2.name)
# print("s3=",s3.collegename,"...",s3.name)
# College.collegename="PCCOE"  #changing static variable
# s1.name="maya"
# print("s1=",s1.collegename,"...",s1.name)
# print("s2=",s2.collegename,"...",s2.name)
# print("s3=",s3.collegename,"...",s3.name)



# #accessing and deleting instance variable from the class
# class Student:
#     def __init__(self):
#         self.name=input("enter name:  ")  #instance variable
#         self.age=20        #instance variable
        
#     def getdata(self):
#         self.s_mb = 987654321

# obj = Student()
# obj.getdata()
# obj.branch="cs"  #adding instance variable by using object
# del obj.age
# print(obj.__dict__)  #printing all instance variable of the object




#instance method,  has parameter a self
#static method,  no parameter self


#static method
class Student:
    #by using class name we can access static method
    @staticmethod   #decorator
    def getinfo(firstname, lastname):
        print("information of student is: ",firstname,lastname)

    @staticmethod
    def printdate(mob,rollno):
        print("information of student is: ",mob,rollno)

Student.getinfo("mahek","bala")  #calling static method
Student.printdate(987654321,101)  #calling static method


#class method to do


