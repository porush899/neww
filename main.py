# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Config
login_time = 30                 # Time for login (in seconds)
new_msg_time = 15                # TTime for a new message (in seconds)
send_msg_time = 15               # Time for sending a message (in seconds)
country_code = 91               # Set your country code
action_time = 2                 # Set time for button click action
# image_path = "C:/Users/lenovo/Downloads/WhatsApp Image 2024-01-29 at 18.00.58.jpeg"        # Absolute path to you image

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Encode Message Text
with open('message.txt', 'r') as file:
    msg = file.read()


# Open browser with default link
link = 'https://web.whatsapp.com/'
driver.get(link)
time.sleep(login_time)


# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)
        # Click on button to load the input DOM
        # if(image_path):
        #     attach_btn = driver.find_element(By.CSS_SELECTOR, '._1OT67')
        #     attach_btn.click()
        #     time.sleep(action_time)
        #     # Find and send image path to input
        #     msg_input = driver.find_elements(By.CSS_SELECTOR, '._2UNQo input')[1]
        #     msg_input.send_keys(image_path)
        #     time.sleep(action_time)
        # Start the action chain to write the message
        actions = ActionChains(driver)
        for line in msg.split('\n'):
            actions.send_keys(line)
            # SHIFT + ENTER to create next line
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)

# Quit the driver
driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# import time

# # Config
# login_time = 20                # Time for login (in seconds)
# new_msg_time = 20                # TTime for a new message (in seconds)
# send_msg_time = 25               # Time for sending a message (in seconds)
# country_code = 91               # Set your country code
# action_time = 2                 # Set time for button click action
# # image_path = "C:/Users/lenovo/Downloads/WhatsApp Image 2024-01-29 at 18.00.58.jpeg"      # Absolute path to you image


# # Create driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # Encode Message Text
# with open('message.txt', 'r', encoding='utf-8') as file:
#     msg = file.read()

# # Open browser with default link
# link = 'https://web.whatsapp.com'
# driver.get(link)
# time.sleep(login_time)

# # Loop Through Numbers List
# with open('number.txt', 'r', encoding='utf-8') as file:
#     for n in file.readlines():
#         num = n.rstrip()
#         link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
#         driver.get(link)
#         time.sleep(new_msg_time)
#         # Click on button to load the input DOM
#         # if(image_path):
#         #     attach_btn = driver.find_element(By.CSS_SELECTOR, '._1OT67')
#         #     attach_btn.click()
#         #     time.sleep(action_time)
#         #     # Find and send image path to input
#         #     msg_input = driver.find_elements(By.CSS_SELECTOR, '._2UNQo input')[1]
#         #     msg_input.send_keys(image_path)
#         #     time.sleep(action_time)
#         # # Start the action chain to write the message
#         actions = ActionChains(driver)
#         for line in msg.split('\n'):
#             actions.send_keys(line)
#             # SHIFT + ENTER to create next line
#             actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
#         actions.send_keys(Keys.ENTER)
#         actions.perform()
#         time.sleep(send_msg_time)

# # Quit the driver
# driver.quit()


# # Packages
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# # Config
# login_time = 30                 # Time for login (in seconds)
# new_msg_time = 5               # Time for a new message (in seconds)
# send_msg_time = 10               # Time for sending a message (in seconds)
# country_code = +91               # Set your country code
# action_time = 2                 # Set time for button click action
# # image_path = 'image.png'        # Absolute path to you image
# a=['9520344369',
# '9650017061',
# '8273810283',
# '9621223646',
# '9650017061'
# ]

# # Create driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # Encode Message Text
# with open('message.txt', 'r') as file:
#     msg = file.read()

# # Open browser with default link
# link = 'https://web.whatsapp.com'
# driver.get(link)
# time.sleep(login_time)

# # Loop Through Numbers List
# with open('a', 'r') as file:
#     for n in file.readlines():
#         num = n.rstrip()
#         link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
#         driver.get(link)
#         time.sleep(new_msg_time)
#         # Click on button to load the input DOM
#         # if(image_path):
#         #     attach_btn = driver.find_element(By.CSS_SELECTOR, '._1OT67')
#         #     attach_btn.click()
#         #     time.sleep(action_time)
#         #     # Find and send image path to input
#         #     msg_input = driver.find_elements(By.CSS_SELECTOR, '._2UNQo input')[1]
#         #     msg_input.send_keys(image_path)
#         #     time.sleep(action_time)
#         # # Start the action chain to write the message
#         actions = ActionChains(driver)
#         for line in msg.split('\n'):
#             actions.send_keys(line)
#             # SHIFT + ENTER to create next line
#             actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
#         actions.send_keys(Keys.ENTER)
#         actions.perform()
#         time.sleep(send_msg_time)

# # Quit the driver
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from urllib.parse import quote
# import time

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# with open ('message.txt', 'r') as file:
#     msg = file.read()

# msg = quote(msg)
# numbers = []
# with open('numbers.txt', 'r') as file:
#     for num in file.readlines():
#         numbers.append(num.rstrip())


# link = 'https://web.whatsapp.com'
# driver.get(link) 
# time.sleep(15)

# for num in numbers:
#     link = f'https://web.whatsapp.com/send/?phone=+91{num}&text={msg}'
#     driver.get(link)
#     time.sleep(5)
#     action = ActionChains(driver)
#     action.send_keys(Keys.ENTER)
#     action.perform()
#     time.sleep(5)
# time.sleep(2000) 

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import csv

# driver = webdriver.Chrome()

# baseurl = "https://web.whatsapp.com"
# driver.get(baseurl)

# time.sleep(10)

# with open("contacts.csv", newline='')as csvfile:
#     readContacts = csv.reader(csvfile)
#     for phone,msg in readContacts:
#         phonenum = phone
#         message = msg

#         sameTab = (baseurl + "/send?phone= " + str(phonenum))

#         driver.get(sameTab)

#         time.sleep(8)
#         content = driver.switch_to.active_element
#         content.send_keys(message)

#         content.send_keys(Keys.RETURN)      
#         time.sleep(8)
 

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from urllib.parse import quote
# import os

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

# os.system("")
# os.environ["WDM_LOG_LEVEL"] = "0"
# class style():
#     BLACK = '\033[30m'
#     RED = '\033[31m'
#     GREEN = '\033[32m'
#     YELLOW = '\033[33m'
#     BLUE = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN = '\033[36m'
#     WHITE = '\033[37m'
#     UNDERLINE = '\033[4m'
#     RESET = '\033[0m'

# print(style.BLUE)
# print("**********************************************************")
# print("**********************************************************")
# print("*****                                               ******")
# print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
# print("*****      This tool was built by Anirudh Bagri     ******")
# print("*****           www.github.com/anirudhbagri         ******")
# print("*****                                               ******")
# print("**********************************************************")
# print("**********************************************************")
# print(style.RESET)

# f = open("numbers.txt", "r", encoding="utf8")
# message = f.read()
# f.close()

# print(style.YELLOW + '\nThis is your message-')
# print(style.GREEN + message)
# print("\n" + style.RESET)
# message = quote(message)

# numbers = []
# f = open("numbers.txt", "r")
# for line in f.read().splitlines():
# 	if line.strip() != "":
# 		numbers.append(line.strip())
# f.close()
# total_number=len(numbers)
# print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
# delay = 30

# driver = webdriver.Chrome(ChromeDriverManager().install(), Options=options)
# print('Once your browser opens up sign in to web whatsapp')
# driver.get('https://web.whatsapp.com')
# input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
# for idx, number in enumerate(numbers):
# 	number = number.strip()
# 	if number == "":
# 		continue
# 	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
# 	try:
# 		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
# 		sent = False
# 		for i in range(3):
# 			if not sent:
# 				driver.get(url)
# 				try:
# 					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
# 				except Exception as e:
# 					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
# 					print("Make sure your phone and computer is connected to the internet.")
# 					print("If there is an alert, please dismiss it." + style.RESET)
# 				else:
# 					sleep(1)
# 					click_btn.click()
# 					sent=True
# 					sleep(3)
# 					print(style.GREEN + 'Message sent to: ' + number + style.RESET)
# 	except Exception as e:
# 		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
# driver.close()