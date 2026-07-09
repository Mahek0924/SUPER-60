# import re
# count = 0
# pattern = re.compile("function")  #string converts to bytecode
# # print(pattern)
# matcher = pattern.finditer('''A function in python is defined by a def statement.
#                            python The general syntax looks like this: def function-name(parameter list):
#                            statements, i.e. the function body. The parameter python list consists of none 
#                            or more parameters''')
# # print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences: ",count)



#----------------------------------------------------------------



# import re
# count=0
# matcher = re.finditer("Hi","HiHiHiHi")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences: ",count)



#-------------------------



# import re
# obj = input("enter any character: ")
# objmatch = re.finditer(obj,"a7b @k9z")
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())


#--------------------------------------

# import re
# match = re.findall('[^0-9a-zA-z]',"abch3hdh5bk7ZQ$&*")
# print(match)

#------------------------------------------

# # sub() function
# import re
# obj = re.sub('[a-zA-z]','*',"2345 abcd ABCf deff")
# print(obj)


#---------------------------------------------


# import re
# s=input("enter email id: ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@sitrc[.]org",s)
# if m!=None:
#     print("valid")
# else:
#     print("invalid")



#--------------------------------------------
# pattern search in file.txt
import re
a = input("enter string to perform match operation: ")
f = open("myfile.txt", 'r')
c = f.read()
mtch = re.search(a, c)
print(mtch)
if mtch != None:
    print("match found at begining level")
    print(mtch.start(), "-", mtch.end())
else:
    print("there is no matching at begining level")