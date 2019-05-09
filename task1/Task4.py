"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

texts_allnums=list()
calls_callers=list()
calls_receivers=list()
telemarket_list=list()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        texts_allnums.append(text[0])
        texts_allnums.append(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        calls_callers.append(call[0])
        calls_receivers.append(call[1])

    for caller in calls_callers:
        if not caller in texts_allnums:
            if not caller in calls_receivers:
                telemarket_list.append(caller)

print("These numbers could be telemarketers:")
print(*sorted(set(telemarket_list)),sep='\n')

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

