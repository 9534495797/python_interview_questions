arr = [1,2,3,4,5,6,7,9,10]
missing_elements = []
for element in range(arr[0], arr[-1]+1):
    if element not in arr:
        missing_elements.append(element)
print(missing_elements)