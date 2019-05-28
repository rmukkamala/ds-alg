

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




msg= "The bird is the word"
hash=frequency(msg)
print(sort_frequency(hash))



# list1 = [(1, 2), (3, 3), (5, 1)]
# list1.sort()
# print(list1)