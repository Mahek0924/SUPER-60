a={(1,2):1, (2,3):2, (4,5):3}
print(a[4,5])
#3



a={'a':1, 'b':2, 'c':3}
print(a['a','b'])
#key error



fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))
#3



arr= {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1
sum=0
for k in arr:
    sum += arr[k]
print(sum)
#4  key value update



arr1= {}
arr1[1] = 1
arr1['1'] = 2
arr1[1.0] += 4
sum1=0
for k in arr1:
    sum += arr1[k]
print(sum1)
#6  key value update



mydict = {}
mydict[(1,2,4)] = 8
mydict[(4,2,1)] = 10
mydict[(1,2)] = 12
sum=0
for k in mydict:
    sum += mydict[k]
print(sum)
print(mydict)
#30
#{(1,2,4):12 , (4,2,1):10 , (1,2):8}  key value update




box={}
jars={}
crates={}
box['biscuit']=1
box['cake']=3
jars['jam']=4
crates['box']=box
crates['jars']=jars
print(len(crates[box]))
#type error, because box is not a key in crates, it is a value. The correct way to access the length of the box dictionary would be len(crates['box']).


dict = {}



rec={"name":1,"age":2}
id1 = id(rec)
del rec
rec={"name":1,"age":2}
id2 = id(rec)
print(id1 == id2)
