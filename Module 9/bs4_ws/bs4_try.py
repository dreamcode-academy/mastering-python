import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://books.toscrape.com/"

def fetch_html(url):
    """ Fetch the HTML content from the URL """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')

def scrape_books(html_content):
    """ Parse HTML content and extract book details """
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all book containers on the page
    books = soup.find_all('article', class_='product_pod')

    # List to store scraped data
    scraped_data = []

    # Extracting data from each book container
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        scraped_data.append({'title': title, 'price': price, 'availability': availability})

    return scraped_data

# Fetch HTML content from the website
html_content = fetch_html(url)

# Check if HTML content was successfully fetched
if html_content:
    # Scrape books data
    book_data = scrape_books(html_content)
    for book in book_data:
        print(f"Title: {book['title']}, Price: {book['price']}, Availability: {book['availability']}\n") # Display the first 5 books for demonstration
else:
    print("Failed to fetch HTML content from the website")
