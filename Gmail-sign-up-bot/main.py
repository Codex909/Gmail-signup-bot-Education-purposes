import os
import time
from random import randint
import random
import string
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome, ChromeOptions
from fake_useragent import UserAgent 
 # Import the UserAgent class
 
# Path to the text file containing first names and last names
txt_file_path = 'names.txt'

# Open the text file and read the names
with open(txt_file_path, 'r') as file:
    names = file.readlines()

# Remove any whitespace characters from the names
names = [name.strip() for name in names]

# Set Chrome options with proxy configuration
options = ChromeOptions()
options.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Replace with the actual path to Chrome executable
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False) 

# Iterate over the names and sign up for Gmail accounts
for name in names:
    first_name, last_name = name.split()

    # Inside the loop, create a new UserAgent instance for each request
    user_agent = UserAgent().random
    options.add_argument(f'user-agent={user_agent}')

    # Launch Chrome driver with the configured options
    with Chrome(options=options) as driver:
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.get('https://accounts.google.com/signup/v2/createaccount?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp')
        time.sleep(11)
    

    # Fill in the first name
    first_name_field = driver.find_element(By.ID, 'firstName')
    first_name_field.send_keys(first_name)
    time.sleep(4)

    # Fill in the last name
    last_name_field = driver.find_element(By.ID, 'lastName')
    last_name_field.send_keys(last_name)
    time.sleep(3)

    # Click the "Next" button
    next_button = driver.find_element(By.ID, 'collectNameNext')
    next_button.click()
    time.sleep(8)

    # Select random month from the drop-down
    month_dropdown = driver.find_element(By.ID, 'month')
    month_options = month_dropdown.find_elements(By.TAG_NAME, 'option')
    random_month_index = randint(1, len(month_options) - 1)
    month_options[random_month_index].click()
    time.sleep(6)

    # Write a random day in the day box
    day_input = driver.find_element(By.ID, 'day')
    day_input.clear()
    random_day = randint(1, 28)
    day_input.send_keys(str(random_day))
    time.sleep(3)

    # Write a random year older than 2000 in the year box
    year_input = driver.find_element(By.ID, 'year')
    year_input.clear()
    random_year = randint(1995, 2000)
    year_input.send_keys(str(random_year))
    time.sleep(2)

    # Set gender to the third option using JavaScript
    script = "var genderOptions = arguments[0].getElementsByTagName('option'); " \
             "genderOptions[3].selected = true;"
    driver.execute_script(script, driver.find_element(By.ID, 'gender'))

    # Click the "Next" button
    next_button = driver.find_element(By.ID, 'birthdaygenderNext')
    next_button.click()
    time.sleep(5)

    suggested_email = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]/div/div[1]/div/div[3]/div')
    suggested_email.click()
    time.sleep(3)

    # Click the "Next" button
    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(5)

    # Read passwords from 'passwords.txt' file
    with open('passwords.txt', 'r') as passwords_file:
        passwords = passwords_file.readlines()

    # Remove any whitespace characters from the passwords
    passwords = [password.strip() for password in passwords]

    # Select the password box
    password_box = driver.find_element(By.NAME, 'Passwd')
    password_box.click()
    time.sleep(3)

    # Write the password in the password box
    password_box.send_keys(passwords[0])
    time.sleep(4)

    # Select the confirm password box
    confirm_password_box = driver.find_element(By.NAME, 'PasswdAgain')
    confirm_password_box.click()
    time.sleep(2.3)

    # Write the password in the confirm password box
    confirm_password_box.send_keys(passwords[0])
    time.sleep(2.5)

    # Click the "Next" button
    next_button = driver.find_element(By.ID, 'createpasswordNext')
    next_button.click()
    time.sleep(20.5)

    # Do any other necessary form filling here (e.g., password, etc.)

    # Print the names of the accounts signed up
    print(f"Signed up: {first_name} {last_name}")

# Close the webdriver
driver.quit()
