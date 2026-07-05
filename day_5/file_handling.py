# whenerver we want to use data in the future that time we use file handling , 
# or store data for future purpose

# f = open("myfile.txt","w")
# print("name of file :",f.name)
# print("file mode :",f.mode)
# print("readable :",f.readable())
# print("writable :",f.writable())
# print("file closed :",f.closed)
# f.close()
# print("file closed :",f.closed)


#-----performing write operation
# f = open("myfile.txt","w")
# f.write("\npune is a smart city")
# f.write("\nnagpur is a smart city")
# f.write("\nbanglore is a smart city")
# f.write("\nnashik is a smart city")
# f.close()
# print("write operation done")


#------performing append mode, it does not overwrite
# f = open("myfile.txt","a")
# f.write("\nindore is a smart city")
# f.write("\nnagpur is a smart city")
# f.write("\nbanglore is a smart city")
# f.write("\nnashik is a smart city")
# f.close()
# print("append operation done")



# # --------inserting list
# f = open("myfile.txt","w")
# mylist=['\nmahek','\npranav','\ngauri']
# f.writelines(mylist)
# f.close()
# print("written  multiple lines")




# #-------------- read mode
# f = open("myfile.txt","r")
# print(f.read())
# f.close()


# with keyword
# with open("myfile.txt","w") as f:
#     f.write("mahek\t")
#     f.write("uttam\t")
#     f.write("bala\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)



# with open("myfile.txt","r") as f:
#     content=f.read()
#     print(content)


# #------------binary file modes
# f1 = open("ss.jpg","rb")
# f2 = open("ss1.jpg","wb")
# data = f1.read()
# f2.write(data)
# print("New image is available")




# ------------- csv files
# import csv 
# f = open("Student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(['StudentID','rollno','name','mobileno'])
# studentid=int(input("enter student id:"))
# rollno=int(input("enter roll number:"))
# name=input("enter name:")
# mobileno=int(input("enter mobile no:"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record saved")


#----------------------------------------------
# accept input from user rollno, name, mobileno, p1,p2,p3, email
# calculate total, percentage
import csv 
# f = open("Data.csv","a",newline="")
# a = csv.writer(f)
# a.writerow(['rollno','name','mobileno','p1','p2','p3','email','total','percentage','status'])
# rollno=int(input("enter roll number:"))
# name=input("enter name:")
# mobileno=int(input("enter mobile no:"))
# p1=int(input("enter p1 marks:"))
# p2=int(input("enter p2 marks:"))
# p3=int(input("enter p3 arks:"))
# email=input("enter email:")
# total=p1+p2+p3
# percentage=total/3.0
# status=""
# if p1>=40 and p2>=40 and p3>=40:
#     status=status+"pass"
# else:
#     status=status+"fail"

# a.writerow([rollno,name,mobileno,p1,p2,p3,email,total,percentage,status])
# print("student record saved")
