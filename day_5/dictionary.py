# mydict= {
#     101:"prashant",
#     102:"advik",
#     "103":"mohini",
#     "104":"trivani",
#     101:"advik",
#     104:"advik"
# }

# print(mydict)
# print(type(mydict))   #type of data structure variable


#with the help of key we can print value
# a = mydict[102]
# print(a)


# replace old value by new value using key
# mydict[102] = "peter"
# print(mydict)


#by default looping statement access keys
#to print keys in the dictionary
# for x in mydict:
#     print(x)


#to print values in the dictionary
# for x in mydict.values():
#     print(x)


#to print both keys and values both
# for x,y in mydict.items():
#     print(x,y)


#to add new key value pair in a dictionary
# mydict["mobile no"] = 1234567876
# print(mydict)

#--------------------------------------------------------

# mydict = {
#     101:"mahek",
#     "profession":"developer",
#     "empid":1001
# }

# #pop() is used to remove key value pair using key name
# mydict.pop(101)
# print(mydict)



# mydict = {
#     101:"mahek",
#     "profession":"developer",
#     "empid":1001
# }

# #copy() is used to copy whole dictionary with different memory address
# newdict =mydict.copy()
# print(id(mydict))
# print(id(newdict))
# print(newdict)





#-----------------------------  to check if list is empty or not
mydict={}
if mydict.__len__() == 0:   # to check length
    print("empty")
else:
    print("dictionary has elements")


#---------------------------------------  check maximum value and return key
# def check_max(mydict):
#     max=0
#     for i in mydict:
#         v = mydict[i]
#         if v>max:
#             max=v 
#     for key,value in mydict.items():
#         if value == max:
#             return key
        
# def check_max(mydict):
#     max=0
#     for i in mydict:
#         if mydict[i]>max:
#             max=mydict[i] 
#     for key,value in mydict.items():
#         if value == max:
#             return key

# new={'a':10 , 'b':20 , 'c': 30 , 'd':5}
# print(check_max(new))


#--------------------------------------------- reverse a dictionary key-value > value-key
# def dict_reverse(mydict):
#     newdict={}
#     for key,value in mydict.items():
#         newdict[value]=key
#     return newdict

# new={'a':10 , 'b':20 , 'c': 30 , 'd':5}
# print(dict_reverse(new))



#------------------------------------------find common key-value pairs in teo dictionaries
# def common_keyvale(dict1,dict2):
#     newdict={}
#     for key1,value1 in dict1.items():
#         for key2,value2 in dict2.items():
#             if key1==key2 and value1==value2:
#                 newdict[key1]=value1
#     return newdict

# d1={'a':1 , 'b':2 , 'c':3}
# d2={'b':2 , 'c':4 , 'd':5}
# print(common_keyvale(d1,d2))





