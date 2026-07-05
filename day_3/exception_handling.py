# try:
#     a= int(input("Enter value of a : "))
#     b= int(input("Enter value of b : "))
#     print(a/b)
# except ZeroDivisionError:
#     print("zero division error")
# except ValueError as message:
#     print("Enter only integer value ")





# try:
#     a= int(input("Enter value of a : "))
#     b= int(input("Enter value of b : "))
#     print(a/b)
# except ZeroDivisionError as message:
#     print("zero division error", message)
# except ValueError as message:
#     print("Enter only integer value ", message)







# multiple exception handling with single exception block
# try:
#     a= int(input("Enter value of a : "))
#     b= int(input("Enter value of b : "))
#     print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#     print( message)





# default except block concept
# default except block should be at last
# try:
#     a= int(input("Enter value of a : "))
#     b= int(input("Enter value of b : "))
#     print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#     print("Enter correct message:", message)
# except:
#     print("This is default part of except block")





# we can use else block if there is no error in the input
# try:
#     a= int(input("Enter value of a : "))
#     b= int(input("Enter value of b : "))
#     print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#     print("Enter correct message:", message)
# else:
#     print("Everthing ok")









# #finally
# try:
#     a= int(input("Enter value of a : "))
#     b= int(input("Enter value of b : "))
#     print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#     print("Enter correct message:", message)
# finally:
#     print("always execute")







#finally with else
# try:
#     a= int(input("Enter value of a : "))
#     b= int(input("Enter value of b : "))
#     print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#     print("Enter correct message:", message)
# else:
#     print("no error")
# finally:
#     print("always execute")










#user defined exception  by raise keyword
bank_bal = int(input("enter balance: "))
if bank_bal<2000:
    raise Exception("Account balace is below limit")
else:
    print("Your amount is ", bank_bal)