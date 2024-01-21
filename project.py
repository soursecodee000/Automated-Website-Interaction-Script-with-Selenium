import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def automate_website(url):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # Add any additional options you may need

    # Specify the path to ChromeDriver directly in the webdriver.Chrome() constructor
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print(f"Opening {url}")
        driver.get(url)

        # Wait for the video to start (adjust sleep time as needed)
        time.sleep(60)  # Adjust sleep time to wait for the video to start

        # Click on the button with ID "b6fde059de50615d643a2c178be54c4f3"
        button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'b6fde059de50615d643a2c178be54c4f3'))
        )
        button_element.click()

        # Play the video for a duration between 30s to 1.5min
        play_duration = 30 + (time.time() % 60)  # A random value between 30s to 1.5min
        print(f"Playing video for {play_duration} seconds")
        time.sleep(play_duration)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Stacktrace:")
        traceback.print_exc()

    finally:
        # Close the browser
        print("Closing the browser")
        driver.quit()

# Read links from the text file
with open('Links_list.txt', 'r') as file:
    links = [line.strip() for line in file]

# Number of times to repeat the process
for _ in range(1000):
    for link in links:
        automate_website(link)
