# for i in range(1,4):       #outer loop => rows
#     for j in range(1,4):    #innerloop => columns
#         print(i,end =" ")
#     print("")


#-------------------------------

# n=int(input("enter number of rows:"))
# for i in range(1,n+1):       #outer loop => rows
#     for j in range(1,n+1):    #innerloop => columns
#         print(i,end =" ")
#     print("")

#------------------------------------

# n=int(input("enter number of rows:"))
# for i in range(1,n+1):       #outer loop => rows
#     for j in range(1,n+1):    #innerloop => columns
#         print(n+1-i,end =" ")
#     print("")


#-----------------------------

# n=int(input("enter number of rows:"))
# for i in range(1,n+1):  
#     print("* "*i)           #TIME COMPLEXITY LESS THAN O(N^2) i.e. double loop


#------------------------

# n=int(input("enter number of rows:"))
# for i in range(1,n+1):       #outer loop => rows
#     for j in range(1,1+i):    #innerloop => columns
#         print(chr(64+i),end =" ")
#     print("")


#-------------------------------------------

# n=int(input("enter number of rows:"))
# for i in range(1,n+1):       #outer loop => rows
#     for j in range(1,n+2-i):    #innerloop => columns
#         print(chr(64+j),end =" ")
#     print("")

#--------------------------------------

# import time
# n=int(input("enter number of rows:"))
# for i in range(1,n+1):       #outer loop => rows
#     for j in range(1,n+2-i):    #innerloop => columns
#         time.sleep(2)
#         print(n+1-i,end =" ")
#     print("")


#------------------------------------

# n=int(input("enter number of rows:"))
# for i in range(1,n+1):       #outer loop => rows
#     for j in range(1,n+2-i):    #innerloop => columns
#         print(chr(65+n-i),end =" ")
#     print("")

#---------------------------

import time
n=int(input("enter number of rows:"))
for i in range(1,n+1):       #outer loop => rows
    print(" "*(n-i), end= " ")
    for j in range(1,i+1):    #innerloop => columns
        time.sleep(1)
        print("*",end =" ")
    print("")



