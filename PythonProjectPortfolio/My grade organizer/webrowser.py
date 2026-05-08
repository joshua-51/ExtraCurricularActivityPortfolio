from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

path = "/Users/3041067/Desktop/Python/My grade organizer/chromedriver"

options = webdriver.ChromeOptions()

# 1. This is the most important part for School Macs:
options.add_argument("--remote-debugging-port=9222") 
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# 2. This prevents Chrome from detecting it's being controlled by a bot
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

service = Service(executable_path=path)

try:
    print("Attempting to bypass security and reach the site...")
    driver = webdriver.Chrome(service=service, options=options)
    
    # We use a longer timeout in case the school network is slow
    driver.set_page_load_timeout(30)
    
    driver.get("https://www.google.com")
    print("Victory! Page loaded.")
    
    time.sleep(10)
finally:
    driver.quit()

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="/Users/3041067/Desktop/Python/My grade organizer/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(10)

driver.quit()
"""