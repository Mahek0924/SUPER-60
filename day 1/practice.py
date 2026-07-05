#wipro ques
num=578378923
frequency={
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0
}
length = len(str(num))
for i in range(length):
    digit = num % 10
    frequency[digit] += 1
    num //= 10

count=0
for j in range(length):
    if frequency[j] > 1:
        count+=1

print(count)



# q-1
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
#[1,3,5,7,9]

# q-2
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)
#value-error

#q3
a=[1,2,3,4,5]
print(a[3:0:-1])
#[4,3,2]

#arguments type
#positional, default, keyword, variable-length(variable-number)

#q4
#def func(value,values):
#3,44

#q5
arr1=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
for i in range(0,4):
    print(arr1[i].pop())
# 4 7 11 15


#list alising