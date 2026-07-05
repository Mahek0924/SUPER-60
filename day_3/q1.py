# input(1,2,3,4)
# output(24,12,8,6)

arr = [1,2,3,4]
arr2= []
length = len(arr)
for i in range(length):
    product=1
    for j in range(length):
        if (i!=j):
            product*=arr[j]
    arr.append(product)
print(tuple(arr2))