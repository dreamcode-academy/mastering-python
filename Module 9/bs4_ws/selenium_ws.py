from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#url = 'https://www.dreamcode.io/'
#driver.get(url)
#driver.implicitly_wait(10)

url = 'http://quotes.toscrape.com/js/'
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

quotes= driver.find_elements(By.CLASS_NAME, 'quote')

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, 'text').text
    author = quote.find_element(By.CLASS_NAME, 'author').text

try:
    author_link = quote.find_element(By.CSS_SELECTOR, '.author + a').get_attribute('href')
except NoSuchElementException:
    author_link = "Not Available"

print(f'"{text}" - {author} \nAuthor link: {author_link}\n')

print("All URLs from the page")
links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    url_page = link.get_attribute('href')
    if url_page:
        print(f'URL: {url_page}') 

driver.quit()