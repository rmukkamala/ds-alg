
"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. 
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
Bonus Challenge: Is it possible to find the max and min in a single traversal?
Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    print(f"input arr is {ints}")
    max=0
    min=len(ints)-1
    for i in range(1,len(ints)):
        if ints[i]>ints[max]:
            temp=ints[i]
            ints[i]=ints[max]
            ints[max]=temp
        if ints[i]<ints[min]:
            temp=ints[i]
            ints[i]=ints[min]
            ints[min]=temp
    #print(f"max value is {ints[max]}")
    #print(f"min value is {ints[min]}")
    return(ints[min],ints[max])
   

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
m = [i for i in range(981, 10005)]  # a list containing 981 - 10004
n = [i for i in range(49, 102)]  # a list containing 49 - 101
random.shuffle(l)
random.shuffle(m)
random.shuffle(n)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((981, 10004) == get_min_max(m)) else "Fail")
print ("Pass" if ((49, 101) == get_min_max(n)) else "Fail")