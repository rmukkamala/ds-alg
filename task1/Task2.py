"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
calls_dict=dict()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        caller=call[0].strip()
        receiver=call[1].strip()
        time_spent=int(call[3].strip())
        if caller in calls_dict.keys():
            calls_dict[caller] +=time_spent
        else:
            calls_dict[caller]=time_spent
        if receiver in calls_dict.keys():
            calls_dict[receiver] +=time_spent
        else:
            calls_dict[receiver]=time_spent
   

max_key=max(calls_dict, key=calls_dict.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key,calls_dict[max_key]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

