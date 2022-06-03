from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Import Local Modules
import internet

###########################################################

# Stop program if internet already connected
if internet.ping():
    print('Already connected!')
    exit()

# Stop program if default ip address is not target of wifi auto login
target_ip = '192.168.10.1'
if internet.defaultGateway() != target_ip:
    print('Unknown Default Gateway! ' + internet.defaultGateway())
    exit()

print('Automating wifi login...')

# enter the link to the website you want to automate login.
website_link = "http://192.168.10.1/login"
# enter your login username
username = "widian"
# enter your login password
password = "widian"

###########################################################

# enter the element for username input field
element_for_username = "username"
# enter the element for password input field
element_for_password = "password"
# enter the element for submit button
element_for_submit = "submit"

###########################################################

# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
# browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]
# uncomment this line,for chrome users
browser = webdriver.Chrome(service=Service('./chromedriver'))
browser.get((website_link))

try:
    username_element = browser.find_element(
        by=By.CSS_SELECTOR, value='[name=username].text')
    username_element.send_keys(username)
    password_element = browser.find_element(
        by=By.CSS_SELECTOR, value='[name=password].password')
    password_element.send_keys(password)
    signInButton = browser.find_element(
        by=By.CSS_SELECTOR, value='[name=submit]')
    signInButton.click()

    #### to quit the browser uncomment the following lines ####
    # time.sleep(3)
    # browser.quit()
    # time.sleep(1)
    # browserExe = "Safari"
    # os.system("pkill "+browserExe)
    # Close gnome shell portal helper window
    os.system('killall gnome-shell-portal-helper')
except Exception:
    # This exception occurs if the element are not found in the webpage.
    print("Some error occured :(")

    #### to quit the browser uncomment the following lines ####
    # browser.quit()
    # browserExe = "Safari"
    # os.system("pkill "+browserExe)
