
class TrieNode:
    def __init__(self):
        self.children={}
        self.isLast=False


class Trie:
    def __init__(self):
        self.root= TrieNode()
    
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

    def all_suffix_old(self,word):
        result=list()
        char=''
        curr=self.root
        for ch in word:
            #while 
            if ch not in curr.children:
                return result
            char+=ch
            curr=curr.children[ch]
        result.append(char)
        return result

    def all_suffixes(self, prefix):
        curr=self.root
        results = set()
        if curr.isLast:
            results.add(prefix)
        if not curr.children: 
            return results
        #return reduce(lambda a, b: a | b, [node.all_suffixes(prefix + char) for (char, node) in self.children.items()]) | results
        #reduce(lambda a, b: a | b, [node.all_suffixes(prefix + char) for (char, node) in self.children.items()]) | results
        for (char, node) in curr.children.items():
            node.all_suffixes(prefix + char)
        return results



    def displayTrie(self):
        curr=self.root
        for ch in curr.children.keys():
            print(curr.children[ch])



 
            

                








arr=['hello','hi','good','morning','mow']
#print(type(arr))

t= Trie()

for entry in arr:
    t.insert(entry)

msg='good'
print(t.contains(msg))

#print(t.displayTrie())

print(t.all_suffixes('h'))


