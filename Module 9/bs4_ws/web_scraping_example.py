from bs4 import BeautifulSoup
import requests

response = requests.get('http://quotes.toscrape.com', timeout=10)

soup = BeautifulSoup(response.content, 'html.parser')

quotes =soup.find_all('span', class_='text')

for quote in quotes:
    print(quote.get_text())