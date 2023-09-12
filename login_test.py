# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create an instance of the webdriver 
driver = webdriver.Chrome()

# (replace 'http://www.mywebsite.com/login' with the actual URL)
driver.get('file:///D:/web.html')

# Wait for the login button to activate before adjusting the timeout as necessary.
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-button')))

# Click the login button
login_button.click()

# Locate the username and password entry fields (replace 'username-field' and 'password-field' with the correct IDs or XPaths).
username_field = driver.find_element(By.ID, 'username-field')
password_field = driver.find_element(By.ID, 'password-field')

# Type the username and password (substituting "your_actual_username" and "your_actual_password" with your real credentials).
username_field.send_keys('your_actual_username')
password_field.send_keys('your_actual_password')

# Submit the login form (instead of "login-form," use the login form's actual ID or XPath).
login_form = driver.find_element(By.ID, 'login-form')
login_form.submit()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome-message')))

welcome_message = driver.find_element(By.ID, 'welcome-message')

# Verify the welcome message to confirm a successful login
if welcome_message.text == 'Welcome, Your Name!':
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser window
driver.quit()
