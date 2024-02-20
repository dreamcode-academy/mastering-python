import re
pattern = re.compile(r"\b[A-Za-z]+\b")
text = "Python and regex"
matches = pattern.findall(text)

for word in matches:
    print("Word match: ", word)
