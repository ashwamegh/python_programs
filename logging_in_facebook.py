#Python 3.6.0

from selenium import webdriver
import time
def fb_login():
    browser= webdriver.Firefox(executable_path=r'C:\geckodriver-v0.14.0-win64\geckodriver.exe')#Your Path to geckodriver
    browser.get('https://facebook.com')
    #Selecting Page Input Elements
    user= browser.find_element_by_css_selector('#email')
    user.send_keys('Your_Email')
    password=browser.find_element_by_css_selector('#pass')
    password.send_keys('Your_Passpword')
    login=browser.find_element_by_css_selector('#loginbutton')
    login.click()

fb_login()
