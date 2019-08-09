
"""
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that 
all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
for e.g. [1, 2, 3, 4, 5]
The expected answer would be [531, 42]. Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, return any one.
Here is some boilerplate code and test cases to start with:
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    tarr=input_list.copy()
    fnum=''
    snum=''
    for i in input_list:
        maxnum=max(tarr)
        tarr.remove(maxnum)
        if i%2==0:
            fnum=str(fnum) + str(maxnum)
        else:
            snum=str(snum) + str(maxnum)
    #print(f"fnum is {fnum} and snum is {snum}")
    return int(fnum), int(snum)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[5, 2, 3, 7, 9], [9532, 7]])
test_function([[1, 5, 3, 6], [653, 1]])
#test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
