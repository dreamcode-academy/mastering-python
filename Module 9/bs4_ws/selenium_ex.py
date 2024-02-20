from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Initialize Chrome options
chrome_options = Options()
# You can add specific options here, for example:
# chrome_options.add_argument("--headless")

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to a website
driver.get('http://example.com')
driver.implicitly_wait(10)

# Close the browser
#driver.quit()
