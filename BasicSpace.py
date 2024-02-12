import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def initialize_browser():
    options = webdriver.ChromeOptions()
    #This makes chrome run in the background:
    # options.add_argument('--headless')
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    browser = webdriver.Chrome(options=options)
    return browser

def wait_for_login_time(target_time):
    current_time = datetime.now().timestamp() # Get the current time as a timestamp
    time_diff = target_time.timestamp() - current_time

    if time_diff > 0:
        time.sleep(time_diff)

def login(browser):
    try:
        with open("login.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if "email" in line:
                    email = line.split("=")[1].strip().strip('"')
                elif "password" in line:
                    password = line.split("=")[1].strip().strip('"')
        
        target_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 17, 00)  # 5:00 PM
        wait_for_login_time(target_time)
        
        browser.get("https://portal.spacebasic.com/login")
        
        email_entry = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        email_entry.clear()
        ActionChains(browser).move_to_element(email_entry).click().perform()
        ActionChains(browser).send_keys(email).perform()
        
        password_entry = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        password_entry.clear()
        ActionChains(browser).move_to_element(password_entry).click().perform()
        ActionChains(browser).send_keys(password).perform()
        
        login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), ' Log In ')]")))
        login_button.click()
        print("Logged in Successfully")
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

        choice_list = []

        for preference in preferences:
            if preference in preference_values:
                choice_list.append(int(preference_values[preference]))

        return choice_list

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    

#uncomment when you get IDs
"""def booking(browser, choice_list):
	try:
		mess_management_dropdown = WebDriverWait(browser, 10).until(
			EC.element_to_be_clickable((By.ID, "dashboard-MessManagement"))
		)
		browser.execute_script("arguments[0].scrollIntoView();", mess_management_dropdown)
		mess_management_dropdown.click()

		booking_option = WebDriverWait(browser, 10).until(
			EC.element_to_be_clickable((By.ID, "BOOKING OPTION ID"))
		)
		browser.execute_script("arguments[0].scrollIntoView();", booking_option)
		booking_option.click()

		
		dropdown_ids = ["1st CHOICE DROPDOWN ID", "2nd CHOICE DROPDOWN ID", "3rd CHOICE DROPDOWN ID"]

		for i in range(len(choice_list)):
			dropdown_id = dropdown_ids[i]
			choice = choice_list[i]

			# Scroll the dropdown into view using JavaScript
			script = f"document.getElementById('{dropdown_id}').scrollIntoView(true);"
			browser.execute_script(script)

			# Select the option in the dropdown
			dropdown_option = WebDriverWait(browser, 10).until(
				EC.element_to_be_clickable((By.XPATH, f"//*[@id='{dropdown_id}']/div/ul/li[{choice}]"))
			)
			dropdown_option.click()

	except Exception as e:
		print("An error occurred in booking():", str(e))"""


def main():
    browser = initialize_browser()
    try:
        login(browser)
        choice_list = booking_choice()
        print(choice_list)
        #booking(browser, choice_list)
    except Exception as e:
        print("An error occurred in main():", str(e))
    finally:
        input("Press Enter to close.")
        browser.quit()

if __name__ == "__main__":
    main()
