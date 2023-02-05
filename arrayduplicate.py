def find(array):
    # Declare an array which will store all the duplicate elements
    duplicate_element_array = []

    # Iterate on the elements of array to find duplicate elements
    for i in array:
        if array.count(i) > 1 and i not in duplicate_element_array:
            duplicate_element_array.append(i)

    # Print all duplicate elements
    print("Duplicate element in an array : ", end="")
    for i in sorted(duplicate_element_array):
        print(i, end=" ")


# declare array
array = [-1, 8, 1, 8, -1, 5, 1, -3]

# print(array)
print("Array= ", array)
find(array)