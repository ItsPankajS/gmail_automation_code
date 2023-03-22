#Below code is for business/SSO login purpose where gmail is used and generally email password is not required, 
#incase of it require, its must to add the line for that as well

from selenium import webdriver 
import time
#from selenium.webdriver.common.action_chains import ActionChains


## Working directory for saving files
#op = r""

#os.chdir(op)

## Importing chrome web driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Pankaj Sharma\Documents\chromedriver.exe") ##### Add the path to chormedriver.exe file, If not available, download it
time.sleep(10)  

## Portal
url="https://mail.google.com/mail/u/0/#inbox"
driver.get(url)
time.sleep(2)

## Entering log in credentials
driver.find_element_by_name("identifier").send_keys("user_login_email@gmail.com")  # Add email for login purpose.
time.sleep(15)
## Click on Next
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(60)
# Click on Continue
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()
time.sleep(10)
# Click on Compose new email
driver.find_element_by_xpath('//*[@id=":ki"]/div/div').click()
time.sleep(15)

from selenium.webdriver.common.keys import Keys
# Give list of recipients
emails = ["user_1@gmail.com",",", "user_2@gmail.com"]
#split funtion will convert string into list split wrt “,”
#emails = emails.split(',')
for email in emails:
    driver.find_element_by_class_name("vO").send_keys(email)
    time.sleep(0.7)
    driver.find_element_by_class_name("vO").send_keys('',Keys.ENTER)
    time.sleep(10)


time.sleep(10)

## Add Subject to your email
subjElem = driver.find_element_by_name("subjectbox")
subjElem.send_keys('Automated Email Testing') #Email Subject

time.sleep(7)
import os
os.chdir(r"C:\Users\User_Name\Documents\Test") #Replace your username here with user_name
with open("Exceptions.txt", 'r', encoding='UTF-8') as f:
    text = f.read()

#Body
driver.find_element_by_css_selector(".Am.Al.editable.LW-avf").click()
driver.find_element_by_css_selector(".Am.Al.editable.LW-avf").clear()
#Add your body content below
body='Hi Team,\n\n This is an automated email. Please ignore it'
driver.find_element_by_css_selector(".Am.Al.editable.LW-avf").send_keys(body)

time.sleep(5)

sendElem = driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3")
sendElem.click()