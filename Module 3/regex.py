import re
r"""
# re.findall()

text = "Call me at 555-1234 or 555-5678 tomorrow"

phone_pattern = r"\d{3}-\d{4}"

match = re.findall(phone_pattern, text)

if match:
    print(match)


#re.match
pattern = r"Hello"
string = " World Hello, "
result = re.match(pattern, string)
if result:
    print("Match found")
else:
    print("Not match")
    """

text = 'The quick brown fox jumps over the lazy dog'


# find the word 'fox'
#if (re.search(r'\bfox\b', text)):
   # print("Found")



# find any three-letter word ending in 'ox'

#print(re.search(r'\b[a-z]ox', text).group())

# find any word starting with 't', 'b' or 'f', 

print(re.findall(r'\b[tbf]\w*', text))

