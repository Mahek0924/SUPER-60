init_tuple= ()
print(init_tuple.__len__())
#it return default value 0

init_tuple_a= 'a','b'
init_tuple_b= ('a','b')
print(init_tuple_a == init_tuple_b)
#returns true, because pyhton considers comma separated value as tuple default and for tuple () in not required

l=[1,2,3]
init_tuple = ('Python',) * (l.__len__ - l[::-1][0])
print(init_tuple)
#()

