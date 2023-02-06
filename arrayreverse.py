from array import *
arr = array('i', [])
n = int(input("enter number of elements"))
for i in range(n):
   arr.append(int(input("enter the array elements")))
print("entered array is:")
for i in range(len(arr)):
   print(arr[i])
print("Array in reverse order: ")
for i in range(len(arr)-1, -1, -1):
   print(arr[i])
