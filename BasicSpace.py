from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os


def initialize_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    browser = webdriver.Chrome(options=options)
    return browser

def login(browser):
    try:
        browser.get("https://portal.spacebasic.com/login")
        phone = input("Phone Number: ")

        # Clicking on the checkbox using JavaScript
        browser.execute_script("document.getElementById('customSwitch1').click();")

        mobile_entry = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='mobile']")))
        mobile_entry.clear()
        ActionChains(browser).move_to_element(mobile_entry).click().perform()
        ActionChains(browser).send_keys(phone).perform()

        generate_otp = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate OTP')]")))
        generate_otp.click()

        otp = input("Enter OTP: ")

        otp_entry = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp"]')))
        otp_entry.clear()
        ActionChains(browser).move_to_element(otp_entry).click().perform()
        ActionChains(browser).send_keys(otp).perform()

        submit_otp = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit OTP')]")))
        submit_otp.click()
        print("Finished Successfully")
          
        time.sleep(2)
    
    except Exception as e:
        print("An error occurred:", str(e))

        
def booking_choice():
    file_path = "preferences.txt"
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            preferences = [line.strip() for line in lines]

        preference_values = {
            "namdhari": "0",
            "hostel mess": "1",
            "food court": "2"
        }

        value = ""

        for preference in preferences:
            if preference in preference_values:
                value += preference_values[preference]

        return value


    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    
def booking(browser, choices):
    
    

def main():
    browser = initialize_browser()
    try:
        login(browser)
        choices = booking_choice()
        print(choices)
        
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        input("Press Enter to close.")
        browser.quit()

if __name__ == "__main__":
    main()
