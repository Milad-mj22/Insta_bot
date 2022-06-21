from selenium import webdriver
# from selenium.webdriver.support import ui
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager as CM
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from time import sleep, strftime
from time import sleep
from random import randint
import pandas as pd
import cv2
# from colorama import Fore , Style
import os
import time
# import random
# import datetime
# import logging
from random import randint
# import instaloader


class insta():
    def __init__(self,path_webdriver) -> None:
        self.path_webdriver=path_webdriver

    def mywebdriver(self):
            
            options = webdriver.ChromeOptions()
            options.add_experimental_option('w3c', True)                 
            options.add_experimental_option("detach", True)
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument('--no-sandbox')
            options.add_argument("--log-level=3")
            mobile_emulation = {
                            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            self.webdriver = webdriver.Chrome(executable_path=self.path_webdriver,options=options)
            cv2.waitKey(1000)
            self.webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            cv2.waitKey(1000)
            permenantcomment='dm for collab 🎁'
            directmessages='Contact our main page  @crescentreasures they have a great offer for you ❤️ they will explain everything to you in detail' + '.' + 'Just send our conversation screenshot for them'
            directmessagescount=0
            os.system('cls')

    def instalogin(self):

            
            
            
            i=randint(0, len(self.idlist)-1)
            

            username = WebDriverWait(self.webdriver, 20).until(lambda webdriver:self.webdriver.find_element_by_name('username'))


            username.click()

            
            
            username.send_keys(self.idlist[i]) 

            
            password = WebDriverWait(self.webdriver, 20).until(lambda webdriver:self.webdriver.find_element_by_name('password'))
            
            password.click()

            password.send_keys(self.idpass[0])

            time.sleep(3)

            self.loginbutton()

        
            os.system('cls') 


            
    def loginbutton(self):

            
            try:
                button_login = WebDriverWait(self.webdriver, 10).until(lambda webdriver:self.webdriver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]'))
                button_login.click()
                os.system('cls')
            except:

                pass
            

                


            sleep(3)

            os.system('cls')
                        
            try:


                notnow = WebDriverWait(self.webdriver, 10).until(lambda webdriver:self.webdriver.find_element_by_xpath('//button[@class="sqdOP yWX7d    y3zKF     "]'))
                notnow.click()
                os.system('cls')

            except:


                pass
                
            try:

                cancelbutton = WebDriverWait(self.webdriver, 10).until(lambda webdriver:self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[3]/button[2]'))
                cancelbutton.click()
                os.system('cls')


            except:

                pass

            try:

                notnow2 = WebDriverWait(self.webdriver, 10).until(lambda webdriver:self.webdriver.find_element_by_xpath('//button[@class="_a9-- _a9_1"]'))
                notnow2.click()
                os.system('cls')


            except:

                pass

if __name__=='__main__':

    insta_obj=insta()
    insta_obj.mywebdriver()
