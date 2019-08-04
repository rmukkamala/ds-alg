
"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
"""
def array_search_helper(start,end,input_list,target):
    if start>end:
        return -1
    mid=(start+end)//2
    if input_list[mid]==target:
        return mid
    if input_list[start]<=input_list[mid]:
        if target<=input_list[mid] and target>=input_list[start]:
            return array_search_helper(start,mid-1,input_list,target)
        return array_search_helper(mid+1,end,input_list,target)
    if target>=input_list[mid] and target<=input_list[end]:
        return array_search_helper(mid+1,end,input_list,target)
    return array_search_helper(start,mid-1,input_list,target)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start=0
    end=len(input_list)-1
    return array_search_helper(start,end,input_list,number)
    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])