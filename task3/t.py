
class TrieNode:
    def __init__(self):
        self.children={}
        self.isLast=False


class Trie:
    def __init__(self):
        self.root= TrieNode()
        self.allwords=[]
    
    def insert(self,word):
        curr=self.root
        for ch in word:
            if ch not in curr.children.keys():
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.isLast=True

    def contains(self,word):
        curr=self.root
        for ch in word:
            if ch not in curr.children.keys():
                return False
            curr=curr.children[ch]
        return curr.isLast

    def suffix_helper(self,node,word):
        if node.isLast:
            self.allwords.append(word)
        for char,node in node.children.items():
            self.suffix_helper(node,word + char)

    def all_suffixes(self,pre):
        curr=self.root
        notThere=False
        word=''
        for char in list(pre):
            if char not in curr.children:
                notThere=True
                break
            word+=char
            curr=curr.children[char]
        word=word[1:]
        #print(type(word))
        if notThere:
            return -1
        elif curr.isLast and not curr.children:
            return -2
        self.suffix_helper(curr,word)
        print(self.allwords)
        return 1






    def all_suffixes_org(self, prefix):
        curr=self.root
        results = set()
        if curr.isLast:
            results.add(prefix)
        if not curr.children: 
            return results
        #return reduce(lambda a, b: a | b, [node.all_suffixes(prefix + char) for (char, node) in self.children.items()]) | results
        #reduce(lambda a, b: a | b, [node.all_suffixes(prefix + char) for (char, node) in self.children.items()]) | results
        for (char, node) in curr.children.items():
            [node.all_suffixes(prefix + char)
        return results



    def displayTrie(self):
        curr=self.root
        for ch in curr.children.keys():
            print(curr.children[ch])



 
            

#arr=['hello','hi','good','morning','mow']
arr= [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
#print(type(arr))

t= Trie()

for entry in arr:
    t.insert(entry)

msg='good'
#print(t.contains(msg))

#print(t.displayTrie())

print(t.all_suffixes('f'))


