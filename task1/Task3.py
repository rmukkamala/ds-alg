"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

bg_pattern= re.compile("^\(080\)")
mobile_pattern= re.compile("^(7|8|9)")
fixedline_pattern= re.compile("^\(0")
telemarketing_pattern= re.compile("^140")
bg_calls_count=0
receiver_codelist=list()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
      if bg_pattern.match(call[0].strip()):
        if bg_pattern.match(call[1].strip()):
          bg_calls_count +=1
        if mobile_pattern.match(call[1].strip()):
          receiver_codelist.append(call[1].split(' ')[0])
        elif fixedline_pattern.match(call[1].strip()):
          receiver_codelist.append(call[1].split(')')[0][1:])
        elif telemarketing_pattern.match(call[1].strip()):
           receiver_codelist.append('140')
bg_calls_percent=(bg_calls_count/len(receiver_codelist))*100
##Part A
print("The numbers called by people in Bangalore have codes:")
print(*sorted(set(receiver_codelist),key=int),sep='\n')
##Part B
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(bg_calls_percent,2)))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
