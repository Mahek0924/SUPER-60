# #single level inheritance
# #in python all things are by default public
# class College:     #parent class
#     def college_name(self):
#         print("college is MIT")

# class Student(College):  #child class      #inheriting College class
#     def student_info(self):
#         print("Name: Mahek")
#         print("Branch: CS")

# obj=Student()   #object create child class
# obj.college_name()
# obj.student_info()




# #multilevel interface
# class College:     #first class
#     def college_name(self):
#         print("college is MIT")

# class Student(College):  #second class      #inheriting College class
#     def student_info(self):
#         print("Name: Mahek")
#         print("Branch: CS")

# class Exam(Student):  #third class      #inheriting Student class
#     def subject(self):
#         print("Exam is on 10th June")

# obj=Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()





# #multiple inheritance
# class SubMarks:
#     math=int(input("Enter marks of math:"))
#     phy=int(input("Enter marks of physics: "))
# class PractMarks:
#     cpract=int(input("Enter marks of c practical: "))

# class Result(SubMarks,PractMarks):
#     def total(self):
#         if self.math>=40 and self.phy>=40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")

# obj=Result()
# obj.total()



# class A:
#     def add(self):
#         print("a")
# class B:
#     def add(self):
#         print("b")
# class C(B,A):
#     def display(self):
#         self.add()

# obj=C()
# obj.display()
