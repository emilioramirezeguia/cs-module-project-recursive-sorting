# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # # base case 1: list is less than or equal to 1, no more values to search from
    # if len(arr) <= 1:
    #     return -1
    # other way of impleenting base case 1:
    if start > end:
        return -1
    # keep track of the middle position in the list
    middle = (start + end) // 2
    # base case 2: target value was found and successfully returned
    if target == arr[middle]:
        return middle
    # recursion: adjust list size and middle value
    elif target < arr[middle]:
        end = middle - 1
        return binary_search(arr, target, start, end)
    else:
        start = middle + 1
        return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
