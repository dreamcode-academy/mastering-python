#Capturing groups ()
import re


'''



pattern = r"(\d{4})-(\d{2})-(\d{2})"

match = re.search(pattern, date_str)

if match:
    print("Year:", match.group(1))
    print("Month:", match.group(2))
    print("Day:", match.group(3))


#Named groups
 
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"

match =re.search(pattern, date_str)

if match:
    print("Year: ", match.group('year'))
    print("Month: ", match.group('month'))
    print("Day: ", match.group('day'))

# Non-capturing groups
date_str = "2023-12-25"   
pattern= r"(?:\d{4})-(\d{2})-(\d{2})"

match =re.search(pattern, date_str)

if match:
    print("Month:", match.group(1))
    print("Day:", match.group(2))

else:
    print("Not match found")

#LOOK-AHEAD
    

pattern = r'\d+(?= example)'
match = re.search(pattern, text)
if match:
    print("Matching number: ", match.group())

#LOOK-BEHIND
text = '12345 example 67890'  
pattern = r'(?<=12345)\s*\w+'
match = re.search(pattern,text)
if match:
    print("Matching word: ", match.group())
    '''

text = "Today date is (2024-12-25)"
pattern = r'(?<=\()\d{4}-\d{2}-\d{2}(?=\))'
match = re.search(pattern,text)
if match:
    print("Match date: ", match.group())