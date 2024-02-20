import re


text = "Python3, regex; advanced"
pattern = r'[;,\s]+'

words = re.split(pattern, text)
print("Separated words: ", words)