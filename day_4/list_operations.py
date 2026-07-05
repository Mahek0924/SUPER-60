#mylist = ["prashant","advik","komal","ankush","aadarsh",77,"sandip",60.52,"prashant"]
# print(mylist)


# mylist[2]="akshay"
# print(mylist)
# #list is mutable


# #in is membership operator
# if "ankush" in mylist:
#     print("yes")
# else:
#     print("no")


# #append()
# mylist.append("harsh")
# print(mylist)

#append and extend both work like same


# #insert()
# mylist.insert(1,"pranav")
# print(mylist)


# #remove()
# mylist.remove("sandip")
# print(mylist)


# # copy
# newlist = mylist.copy()  #cloning
# print(newlist)


#multidimensional list
# mylist1 = [['prashant','jha'], ['85.56'], [440022, "yyy"]]
# print(mylist1)
# #print(mylist[row][col])
# print(mylist1[0][0])  #'prashant'
# print(mylist1[0][1])  #'jha'
# print(mylist1[1][0])  #'85.56'
# print(mylist1[2][0])  #440022
# print(mylist1[2][1])  #"yyy"

# ---------------------
# [          0          1
#     0 = ['prashant','jha']
#     1 = ['85.56']
#     2 = [440022,    "yyy"]
# ]



# #list replication / multiplication
# list1=["mahek","bala"]
# print(list1*2)


# #list concatenation / addition
# l1= [50,25.50]
# l2= [32, 42]
# print(l1+l2)


# list2=[50, 25.5 , "maya"]
# del list2[2]
# del list2
# print(list2)


# list2=[50, 25.5 , "maya"]
# list2.clear()
# print(list2)




# #typecasting string -> list
# name="pranav"
# print(name)
# myname=list(name)  #typecasting
# print(myname)


# l=[1,2,3,4]
# l.reverse()
# print(l)



# mylist=[44,22,77,0,9,88]
# mylist.sort()  #reverse=True
# print(mylist)
#default sorting for number is ascending order
#default sorting for string is alphabetical order
#we should know that list should contain homogenious
#data otherwise will get typeerror
#python2 supported heteregoneous elements sorting but it is discontinued now




# #alising---------------------
# mylist=[1,2,3,4,5]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0]="maya"
# print(mylist)
# print(newlist)