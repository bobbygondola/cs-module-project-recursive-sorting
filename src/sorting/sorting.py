
'''  Merge sort is a sorting algorithm that splits an array into halves 
    until each half has a single element. It then merges the split arrays, 
    returns the merge, and continues up the recursive ladder until the whole sorted array is returned.  '''

def merge_sort(array):                      

    if len(array) <= 1:                         # return if single/empty
        return array

    midpoint = int(len(array) / 2)              # middle of the array

    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])    # left =  everything up to midpoint, right = everything to end past midpoint

    return merge(left, right)                                                   # return merge() to be called later passing in ^^


def merge(left, right):

    result = []                                 
    left_pointer = right_pointer = 0         # also left/right index

    while left_pointer < len(left) and right_pointer < len(right):  # while there are both elements in BOTH arrays

        if left[left_pointer] < right[right_pointer]:   # if element at left pointer in left array is less than right element at right pointer at right array... We know left ele is smaller

            result.append(left[left_pointer])           # append that smaller element so its sorted
            left_pointer += 1

        else:

            result.append(right[right_pointer])         # if element at right pointer in right array is smaller.. append it to the sorted array
            right_pointer += 1

    result.extend(left[left_pointer:])  # taking everything from left array, left pointer to end and extending it to result
    result.extend(right[right_pointer:])

    return result    # new sorted







# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

