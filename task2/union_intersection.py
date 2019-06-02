
"""
1. Create a class Node with instance variables data and next.
2. Create a class LinkedList with instance variable head.
3. The variable head points to the first element in the linked list.
10. Define the function remove_duplicates which removes duplicate elements from the list passed as argument.
11. Define the function find_union which returns the union of the two linked lists passed to it.
12. Define the function find_intersection which returns the intersection of the two linked lists passed to it.
13. Create two instances of LinkedList, append data to them and find their union and intersection.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def duplicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.value)
            copy.append(node)
            current = current.next
        return copy

def remove_duplicates(llist):
    node=llist.head
    prev=None
    lookup=dict()
    while node:
        if node.value in lookup:
            ##delete
            prev.next=node.next
            prev=None
            pass
        else:
            lookup[node.value]=1
        prev=node
        node=node.next


def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None:
        union = llist_2.duplicate()
        remove_duplicates(union)
        return union
    if llist_2.head is None:
        union = llist_1.duplicate()
        remove_duplicates(union)
        return union
    union=llist_1.duplicate()
    last_node=union.head
    while last_node.next is not None:
        last_node=last_node.next
    last_node.next=llist_2.head
    remove_duplicates(union)
    return union

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None or llist_2.head is None:
        return LinkedList()
    curr=llist_1.head
    ref=dict()
    while curr:
        ref[curr.value]=1
        curr=curr.next
    curr2=llist_2.head
    llist_3=LinkedList()
    while curr2:
        if curr2.value in ref:
            llist_3.append(curr2.value)
        curr2=curr2.next
    remove_duplicates(llist_3)
    return llist_3



############Test Cases################

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) #3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 1 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2)) #6 -> 4 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) #3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_3,linked_list_4)) #will return empty linked list


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,8,9,3,35,98,4,8]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6)) #1 -> 8 -> 9 -> 3 -> 35 -> 98 -> 4 -> 8 ->
print (intersection(linked_list_5,linked_list_6)) ##will return empty linked list

