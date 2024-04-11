# added two bugs - Jack Donovan
# bug: if statement should be i!=0, will cause an array index error, high priority
# bug: if statement should be arr[i]==arr[i-1], to test if the ints are repeated, high priority
# Declare funtion
def remove_duplicates(arr):
    arr.sort()
    # Instantiate arrays
    unique_arr = []
    removed_elements = []
    # Loop thru the array
    for i in range(len(arr)):
        if i == 0 and arr[i] != arr[i-1]:
            removed_elements.append(arr[i])
        else:
            removed_elements.append(arr[i])
    return unique_arr, removed_elements

# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr, removed_elements = remove_duplicates(arr)
print("Original array:", arr)
print("Unique array:", unique_arr)
print("Removed elements:", removed_elements)
