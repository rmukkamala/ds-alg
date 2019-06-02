

"""
Here is one type of pseudocode for this coding schema:
Take a string and determine the relevant frequencies of the characters.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.

"""

import sys,string

##get frequency of the chars in the string
def frequency(str):
    freq=dict()
    for char in str:
        freq[char]=freq.get(char,0) + 1
    return freq

#sort the frequencies in a list of tuples
def sort_frequency(freq):
    list_tuples=[]
    keys=freq.keys()
    for key in keys:
        list_tuples.append((freq[key],key))
    list_tuples.sort()
    return list_tuples

##build a tree with tuples
def buildTree(tuples):
    while len(tuples)>1:
        least_two=  tuple(tuples[0:2])
        rest= tuples[2:]
        sum_freq=least_two[0][0] + least_two[1][0]
        tuples= rest + [(sum_freq,least_two)]
        tuples.sort(key=lambda t: t[0])
        #print(tuples)
    return tuples[0]

##filter the frequencies in the tree
def trimTree (tree) :
    p = tree[1]
    #print(p)                                   # ignore freq count in [0]
    if type(p) == type("") : 
        #print(p)
        return p
    else : 
        return (trimTree(p[0]), trimTree(p[1]))

##assign binary codes for the chars
def assignCodes (node, pat='') :
    global codes
    if type(node) == type("") :
        codes[node] = pat                # A leaf. set its code
    else  :                              #
        assignCodes(node[0], pat+"0")    # Branch point. Do the left branch
        assignCodes(node[1], pat+"1") 

##encode the string
def encode (str) :
    global codes
    output = ""
    for ch in str : 
        output += codes[ch]
    return output

##decode the binary string
def decode (tree, str) :
    output = ""
    node = tree
    for bit in str :
        if bit == '0' : 
            node = node[0]   #left branch
        else: 
            node = node[1]    # right branch
        if type(node) == type("") :  
            output += node              
            node = tree          #re-assign       
    return output


def huffman_encoding(data):
    hash=frequency(data)
    tuples=sort_frequency(hash)
    tree=buildTree(tuples)
    trim_tree=trimTree(tree)
    assignCodes(trim_tree)
    return (encode(data),trim_tree)
    

def huffman_decoding(data,tree):
    return decode(tree, data)

if __name__ == "__main__":
    codes = {}

   #test case 1
    print("#####TEST CASE 1#############")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    #test case 2
    print("#####TEST CASE 2#############")
    a_great_sentence = "This is the best day in the entire universe for everyone"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


#test case 3
    print("#####TEST CASE 3#############")
    a_great_sentence = "Hello ! 'What is the deepest point on earth?' "

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
