

Problem 1:
Get the floored square root of a number.
- To achieve O(log(n)) time complexity, we use the binary search algorithm for finding the floored square root of the number. 
- (Using this method, we reduce the data set to be searched into half  for every iteration)

Time complexity:
 O(log n)


Problem 2:
Search in a Rotated Sorted Array
- We apply Binary search algorithm here as well.
- We calculate the mid element in the array and check if the target value matches.
- If not, we check if the start to mid subarray is sorted. 
- If subarray is sorted we recursively apply the binary search on the subarray as well.
- If the subarray is not sorted, we apply binary search on the mid to end subarray recursively.	

Time Complexity:
 O(log n)



Problem 3:
Rearrange Array Elements so as to form two number such that their sum is maximum.
- We first take a list copy of the original array so that original array data is not modified.
- We find the max element in the duplicate array while iterating through the original array. 
- Then remove the maxnum from the duplicate array.
- We consecutively concatenate the maxnum to firstnum and secondnum (which we are supposed to return) each taking turns. (We do this by modulo operation with 2)

Time Complexity: 
O(nlog n)
  


Problem 4:
Dutch National Flag Problem
- We take 3 pointers p1 (low), p2 (mid), p3(high) for this problem.
- P1 and p2 will start at index 0 and p3 will be assigned the last index in the array.
- For every iteration,  until mid p2 pointer <= p3 high, we swap values and increment /decrement p1,p2 and p3 pointers (index values) based on the 0/1/2 array values.   

Time Complexity: 
O(n)


Problem 5:
Autocomplete with Tries
- We implement tires using a hashmap (dictionary)
- Basically, every trie node has a dictionary and a pointer which identifies if it is the last node for the word.
- The trie object is always created with the assignment a root node.
- For word insertion in tries:
 We iterate every letter in the word and check if the letter exists in the trie dictionary, if not create TrieNode for the respective letter and insert it in the applicable node(dictionary).
 For finding all the suffixes of an input  prefix, we use the find and suffix_helpfer method.
- The find method helps in identifying the TrieNode for which has the last prefix letter.
  The suffix_helper method takes in the node provided by find method to get all the relevant suffixes for the relevant TrieNode.
  We use recursion and a class variable all_words to keep track of all the suffixes for the word. 

Time Complexity:
For Insertion: O(n)
For Finding suffixes(Find method): O(n)
   


Problem 6:
Max and Min in an unsorted array
- We assign the max variable to first index and min to last index of the array.
- For every iteration in the array, we compare max index element with current iterated element and swap if the number is greater then max.
- In the same iteration, we also compare min index element with the iterated/swapped(if applicable) element and swap if the number  is less than min.
- After the end of the for loop, we can return the max and min elements.   

Time Complexity: 
O(n)


Problem 7:
Router Problem
- This problem follows the same concepts as in problem 5 (autocomplete Trie)
- For a router Trie Node, we have a dictionary and 2 variables, one for tracking if it is the leaf node and the other for checking the handler name.
- Here, for adding a route handler:
  We take in the route path and handler name as inputs, then we split the route path into a list of individual items with ‘/’ as the separator. 
 Then we iterate through the path list(list of splitted items) and insert each subitem. Each subitem is assigned a new RouteTrieNode if not present already. The handler assigned is ‘None’ by default for all the route nodes (sub items) except for the last one. The last item/node is assigned the handler name.
- For lookup method, we use the find method and navigate to the end node and then print the associated handler name.
  We print None if the handler is not present or if the node is not the last one.

Time Complexity:
Insertion/Add_handler: O(n)
Lookup/find: O(n) 


