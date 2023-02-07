#taking input from the user
string = input("Enter the string : ")
#converting string into list of its characters
strList=list(string) 
#sorting elements of list
sortedString=''.join(sorted(strList)) 
print("String Sorted in ascending order :", sortedString)
