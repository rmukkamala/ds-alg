"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from os.path import dirname, join
current_dir = dirname(__file__)
file_path1=join(current_dir, "./texts.csv")
file_path2=join(current_dir, "./calls.csv")

with open(file_path1, 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
    texts = list(reader)
    print("First record of texts, {} texts {} at time {}".format(texts[0][0],texts[0][1],texts[0][2]))

with open(file_path2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0],calls[-1][1],calls[-1][2],calls[-1][3]))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

