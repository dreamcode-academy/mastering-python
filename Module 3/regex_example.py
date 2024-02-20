import re


sample_text = 'Contact us at info@example.com, support@example.net or call 123-456-7890'

email_pattern = '[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

result = re.findall(phone_pattern, sample_text)


print(result)