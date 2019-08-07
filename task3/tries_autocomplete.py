
"""
Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure 
that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text 
or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which 
represents a prefix.
Give it a try by implementing the TrieNode and Trie classes below!


Finding Suffixes
Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. 
To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that 
exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and 
we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

Using the code you wrote for the TrieNode above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)
"""


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children={}
        self.isLast=False

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root= TrieNode()
        self.allwords=[]
    
    def insert(self,word): 
        ## Add a word to the Trie
        curr=self.root
        for ch in word:
            if ch not in curr.children.keys():
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.isLast=True

    def suffix_helper(self,node,word=''):
        if node.isLast:
            self.allwords.append(word)
        for char,node in node.children.items():
            self.suffix_helper(node,word + char)

    def find(self,prefix):
        curr=self.root
        notThere=False
        for char in list(prefix):
            if char not in curr.children:
                notThere=True
                break
            curr=curr.children[char]
        if notThere:
            print("None found")
            return False
        elif curr.isLast and not curr.children:
            print("None found")
            return False
        self.allwords=list() ##clearing the buffer
        self.suffix_helper(curr)
        print(self.allwords)
        return True

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

##display suffixes
MyTrie.find("f")  # ['un', 'unction', 'actory']
MyTrie.find("a")  # ['nt', 'nthology', 'ntagonist', 'ntonym']
MyTrie.find("h")  # None found
MyTrie.find("t")  # ['rie', 'rigger', 'rigonometry', 'ripod']


""" from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix=''); """