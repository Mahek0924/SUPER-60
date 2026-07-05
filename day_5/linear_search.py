# linear search
# time complexity = O(N)
# space complexity =O(1)

# pseudocode
# - create function with 2 parameters (array, value) 
# - loop throught the array and check if current array element == value
# - if it is exist , returnt the index of the element that is found
# - if the value not exist in array return -1

# def linearsearch(array,target):
#     for i in range(len(array)):
#         if array[i]==target:
#             return i
#     return -1

# array = [1,2,3,4,5,6,7,8,9]
# target = 7
# result = linearsearch(array, target)
# if result != -1:
#     print("element found at index =",result)
# else:
#     print("element not found")



#-----------------------------minimum and maximum elements
# def minmax(arr):
#     min=arr[0]
#     max=0
#     for i in range(len(arr)):
#         if arr[i]>max:
#             max=arr[i]
#     for i in range(len(arr)):
#         if arr[i]<min:
#             min=arr[i]
#     print("maximum=",max,"minimum=",min)

# array=[5,3,9,2,8]
# minmax(array)



#----------------------find majority of element  - element that appears more thann n/2 times in an array
# def majority(arr):
#     n=len(arr)/2
#     for i in range(len(arr)):




#----------------------------------