# membership operator  - used in collection data type
# 1. in
# 2. not in

# name = "mahek"
# print("h" in name)
# print("z" not in name)


# # for loop ------------------
# for i in range(5):  #i=0  , i<5
#     print(i)  #0,1,2,3,4

# for i in range(1,5):  #i=1  , i<5
#     print(i)   #1,2,3,4

# for i in range(1,10,2):  #i=1  , i<10  , i+2(increment)
#     print(i)   #1,3,5,7,9

# for i in range(5,0,-1):  #i=5  , i>0  , i-1(decrement)
#     print(i)   #5,4,3,2,1


# multiplication table
# for i in range(1,11):  #i=0  , i<11
#     print(i*2)   #2,4,6,8,10,12,14,16,18,20


# for i in range(1,11):
#     print(i,"  ",i*2,"  ",i*3,"  ",i*4,"  ",i*5,"  ",i*6,"  ",i*7,"  ",i*8,"  ",i*9,"  ",i*10," \n ")




# list3=[10,20,30,40,50]
# for i in list3:
#     print(i)



# sum of all numbers in list
# l1=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for x in l1:
#     sum=sum+x
# print("sum=",sum)



# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("this is my cart")
#         continue
#     print(i)


# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("this is my cart")
#         break
#     print(i)




# count=0
# for i in range(9):
#     if i%2 == 0:
#         print(i)
#     else:
#         print(i)
#         count+=1
# print("count = ", count)







#######################################
#if loop-------------------------------

# day = input("enter day: ")
# if day=="SATURDAY" or day=="SUNDAY" or day=="saturday" or day=="sunday":
#     print("weekend")
# else:
#     print("working day")



#print(3//2)  #floor division
#print(3/2)   # division



# #REVERSE NUMBER without loop
# num = 123          #321
# a = num%10         #a=3
# num = num//10      #num=12
# b = num%10         #b=2
# c = num//10        #c=1
# rev = a*100 + b*10 + c*1     #300+20+1=321
# print("reverse =",rev)




# 7 number reverse
# num = 1234567
# a = num%10         
# num = num//10      
# b = num%10         
# num = num//10         
# c = num%10         
# num = num//10
# d = num%10         
# num = num//10
# e = num%10         
# num = num//10
# f = num%10        
# g = num//10
# rev = a*1000000 + b*100000 + c*10000 + d*1000 +e*100 +f*10 +g*1     #300+20+1=321
# print("reverse =",rev)




# # wap for change calculation with respect to total amount
# Amount = int(input("please enter amount for withdrawal :"))
# print(" 100 notes =",Amount//100)
# print(" 50 notes  =",(Amount%100)//50)
# print(" 20 notes  =",((Amount%100)%50)//20)
# print(" 10 notes  =",(((Amount%100)%50)%20)//10)
# print(" 5 notes   =",((((Amount%100)%50)%20)%10)//5)
# print(" 2 coins   =",(((((Amount%100)%50)%20)%10)%5)//2)
# print(" 1 coins   =",((((((Amount%100)%50)%20)%10)%5)%2)//1)





##############################################
# nested if else
# # wap to accept three ages and check the maximum age and print

# age1 = int(input("enter value age1 :"))
# age2 = int(input("enter value age2 :"))
# age3 = int(input("enter value age3 :"))

# if(age1>age2):
#     if (age1>age3):
#         print("Age 1 is greater", age1)
#     else:
#         print("Age 3 is greater", age3)
# else:
#     if (age2>age3):
#         print("Age 2 is greater", age2)
#     else:
#         print("Age 3 is greater", age3)



# wap to accept any one character and check if it is uppercase, lowercase, digit, special symbol




#
while(True):
    username = input("Enter username = ")
    password = input("Enter password = ")
    if username==password:
        print("login successful")
        break
    else:
        print("invalid login")