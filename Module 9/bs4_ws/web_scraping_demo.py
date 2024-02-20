from bs4 import BeautifulSoup
import requests
response = requests.get('http://example.com', timeout=10)

#print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.h1)