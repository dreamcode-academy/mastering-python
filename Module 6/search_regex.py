import re

text = "Python is awesome. Python is fun."
pattern = r'Python'
replacement = 'Programming'
new_text = re.sub(pattern, replacement, text)
print("Modified text: ", new_text)
