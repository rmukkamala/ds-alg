"""
 1.	Input:-Number of message with frequency count.
    2.	Output: - Huffman merge tree.
    3.	Begin
    4.	Let Q be the priority queue,
    5.	Q= {initialize priority queue with frequencies of all symbol or message}
    6.	Repeat n-1 times 
    7.	Create a new node Z 
    8.	X=extract_min(Q)
    9.	Y=extract_min(Q)
    10.	Frequency(Z) =Frequency(X) +Frequency(y);
    11.	Insert (Z, Q)
    12.	End repeat 
    13.	Return (extract_min(Q))
    14.	End.

"""


import sys,string
codes=dict()
def frequency(str):
    freq=dict()
    for char in str:
        freq[char]=freq.get(char,0) + 1
    return freq


def sort_frequency(freq):
    list_tuples=[]
    keys=freq.keys()
    for key in keys:
        list_tuples.append((freq[key],key))
    list_tuples.sort()
    return list_tuples

def buildTree(tuples):
    while len(tuples)>1:
        least_two=  tuple(tuples[0:2])
        rest= tuples[2:]
        sum_freq=least_two[0][0] + least_two[1][0]
        tuples= rest + [(sum_freq,least_two)]
        tuples.sort(key=lambda t: t[0])
    return tuples[0]

def trimTree (tree) :
    p = tree[1]                                    # ignore freq count in [0]
    if type(p) == type("") : 
        #print(p)
        return p
    else : 
        return (trimTree(p[0]), trimTree(p[1]))


def assignCodes (node, pat='') :
    global codes
    if type(node) == type("") :
        codes[node] = pat                # A leaf. set its code
    else  :                              #
        assignCodes(node[0], pat+"0")    # Branch point. Do the left branch
        assignCodes(node[1], pat+"1") 


def encode (str) :
    global codes
    output = ""
    for ch in str : output += codes[ch]
    return output

def decode(tree, str) :
    output = ""
    p = tree
    #print(p)
    for bit in str :
        if bit == '0' : 
            #print(p[0])
            k = p[0]     # Head up the left branch
            pass
        else: 
            k = p[1]    # or up the right branch
            pass
        if type(k) == type(""):
            output += k              # found a character. Add to output
            k = tree                 # and restart for next character
    return output

msg= "The bird is the word"
hash=frequency(msg)
tuples=sort_frequency(hash)
#print(tuples)
tree=buildTree(tuples)
print(tree)
trim=trimTree(tree)
assignCodes(trim)

small = encode(msg)
print(small)
original = decode(tree, small)
print(original)

# print("Original text length", len(msg))
# print("Requires %d bits. (%d bytes)" % (len(small), (len(small)+7)/8))
# print("Restored matches original", str == original)


# list1 = [(1, 2), (3, 3), (5, 1)]
# list1.sort()
# print(list1)