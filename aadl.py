import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound

# Path to your chromedriver
CHROME_DRIVER_PATH = 'C:/Users/ramyb/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'  # Update this path

# URL to refresh
URL = 'https://aadl3inscription2024.dz/'

# Sound file path
SOUND_FILE = 'C:/Users/ramyb/Downloads/success-1-6297.mp3'  # Update this path

# Initialize Chrome WebDriver with options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

service = ChromeService(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    while True:
        driver.get(URL)
        
        # Wait for the page to load
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print("Page loaded successfully!")
            playsound(SOUND_FILE)
        except Exception as e:
            print(f"Error loading page: {e}")
        
        # Wait for some time before refreshing
        # time.sleep(2)  # Adjust the sleep time as needed
finally:
    driver.quit()
