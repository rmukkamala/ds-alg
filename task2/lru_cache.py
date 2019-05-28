
"""
Used hash data structure (dict) for accessing the key.
Used queue for tracking/insertion/deletion. Implemented the queue using doubly linked lists.
The above data structures help us in achieving O(1) time complexity
"""

class Node(object):
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.head=None
        self.tail=None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity=capacity
        self.dict=dict()
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict:
            self._remove(self.dict[key])
            self._add(self.dict[key])
            return self.dict[key].value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.dict:
            self._remove(self.dict[key])
        node=Node(key,value)
        self._add(node)
        self.dict[key]=node
        if len(self.dict) > self.capacity:
            next=self.head.next
            self._remove(next)
            del self.dict[next.key]

    def _add(self, node):
        prev=self.tail.prev
        prev.next=node
        self.tail.prev=node
        node.prev=prev
        node.next=self.tail


    def _remove(self, node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(3))      # return -1