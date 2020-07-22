
'''  Merge sort is a sorting algorithm that splits an array into halves 
    until each half has a single element. It then merges the split arrays, 
    returns the merge, and continues up the recursive ladder until the whole sorted array is returned.  '''

def merge_sort(array):

    if len(array) <= 1:
        return array

    midpoint = int(len(array) / 2)

    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left, right)


def merge(left, right):

    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer += 1

        else:

            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result







# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

