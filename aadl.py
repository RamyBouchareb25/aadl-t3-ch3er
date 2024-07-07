import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from playsound import playsound

# Number of tabs
NUM_TABS = 5
# Timeout for waiting for the page to load
TIMEOUT = 5  # in seconds
# Delay between opening each tab
TAB_OPEN_DELAY = 0.5  # in seconds


# Path to your chromedriver executable
CHROME_DRIVER_PATH = 'C:/Users/ramyb/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'  # Update this path

# URL to refresh
URL = 'https://aadl3inscription2024.dz/'

# Sound file path
SUCCESS_SOUND_FILE = './success-1-6297.mp3'  # Update this path
FAILURE_SOUND_FILE = './error-126627.mp3'  # Update this path

# Initialize Chrome WebDriver with options
chrome_options = Options()
# Comment out headless mode for debugging
# chrome_options.add_argument("--headless")

service = ChromeService(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

def keep_browser_open():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Browser session ended manually.")

try:
    while True:
        try:
            driver.get(URL)
            
            # Custom timeout for waiting for the page to load
            timeout = 5  # Timeout in seconds
            try:
                WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                print("Page loaded successfully!")
                playsound(SUCCESS_SOUND_FILE)
                
                # Keep the browser open
                keep_browser_open()
                break  # Exit the loop after keeping the browser open
                
            except TimeoutException:
                print(f"Page took longer than {timeout} seconds to load. Retrying...")
                
        except WebDriverException as e:
            print(f"Error loading page.\nRetrying...")
            # playsound(FAILURE_SOUND_FILE)
            
        
        # Wait for some time before retrying
        # time.sleep(5)  # Adjust the sleep time as needed

finally:
    # Comment out driver.quit() to keep the browser open
    # driver.quit()
    pass
