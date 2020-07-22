# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start <= end:
        middle = (start + end) // 2                                 # Find middle if arr exists and is sorted
        
        if target == arr[middle]:                                   # If target is middle, return
            return middle
        
        elif target < arr[middle]:                  
            return binary_search(arr, target, start, middle - 1)    # if target is less than the middle, recursively go back.
        
        elif target > arr[middle]:                                  # if target is greater than the middle, recursivley step forward
            return binary_search(arr, target, middle + 1, end)

    return -1
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

