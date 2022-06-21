from random import randint
from click import confirm
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import NoSuchElementException
import os
import geckodriver_autoinstaller
import time
import pyperclip
import numpy as np
import random

geckodriver_autoinstaller.install() 

class connection():

    def __init__(self):
        self.get_ip_port()

    def get_ip_port(self):
        myProxy = "154.236.184.70:1976"
        self.ip,self.port=myProxy.split(':')


    def set_init(self):

        profile = FirefoxProfile(r'tor-browser-linux64-11.0.14_en-US/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default')
        profile = webdriver.FirefoxProfile()
        # profile.set_preference('network.proxy.type', 1)
        # profile.set_preference('network.proxy.socks', self.ip)
        # profile.set_preference('network.proxy.http', self.ip)
        # profile.set_preference('network.proxy.http_port', int(self.port))
        # profile.set_preference('network.proxy.socks_port', int(self.port))
        # profile.set_preference('network.proxy.ssl_port', int(self.port))
        # profile.set_preference('network.proxy.https', self.ip)
        # profile.set_preference('network.proxy.https_port', int(self.port))
        # profile.set_preference("network.proxy.socks_remote_dns", False)

        profile.update_preferences()
        self.driver = webdriver.Firefox(firefox_profile= profile)
        # self.driver.set_window_position(0, 0)
        # self.driver.set_window_size(600, 400)
        return self.driver

    def get_url(self,url):

        self.driver.get(url)


    def get_email_address(self,url):
        # //*[@id="i-email"]
        email=self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div[1]/div[1]/div/button')
        email.click()
        email=pyperclip.paste()
        print('email :',email)
        return email

    def get_email_mail_tm(self):
        email=self.driver.find_element_by_xpath('//*[@id="address"]')
        email.click()
        email=pyperclip.paste()
        print('email :',email)
        return email
        
    
    def get_email_address_temp_mail(self):

        email=self.driver.find_element_by_xpath('//*[@id="apptmo"]/div/div[1]/div[1]/div/button')
        email.click()
        email=pyperclip.paste()
        print('email :',email)
        return email

    def confirm_temp_mail(self):

        link = None
        i=0
        while not link:
            try:
                confim_code=self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div[2]/ul/li/a/div/div[1]/div[2]/div[2]/div/div[1]')
                text=confim_code.text
                code=text[0:6]
                
                return code
            except NoSuchElementException:
                print('Cant Eror Retry','-'*10,i)
                i+=1
                time.sleep(2)
                if i >20:
                    break


    def confirm_email(self):
        # //*[@id="apptmo"]/div/div[2]/div[1]/ul/li/div[2]/div
        i=0
        link = None
        while not link:
            
            try:
                confirm_email=self.driver.find_element_by_xpath('//*[@id="apptmo"]/div/div[2]/div[1]/ul/li/div[2]/div')
                confirm_email.click()

                confirm_code=self.driver.find_element_by_xpath('//*[@id="apptmo"]/div/div[2]/div[2]/div[2]/div[1]').text
                print('confirm_code',confirm_code)
                # print('Email Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Email in Web Retry','-'*10,i)
                i+=1
                time.sleep(2)
                if i>30:
                    break
        # try:

        #     # confirm_code=
        # except:
        #     print('eror')
        #     self.confirm_email()
        # # pass

    def change_email(self,get=False):
        
        change_mail=self.driver.find_element_by_xpath('//*[@id="apptmo"]/div/div[1]/div[2]/div[3]/button/span')
        change_mail.click()
        
        change_mail=self.driver.find_element_by_xpath('//*[@id="apptmo"]/div[2]/div/div[3]/button[1]')
        change_mail.click()
        if get:
            self.get_email_address()



    def set_insta_parms(self,mail=None,full_name=None,user=None,password=None,chek_parms=True):
        time.sleep(10)
            # /html/body/div[1]/div/div/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input
        eror=False
        i=0
        link = None
        while not link:
            try:
                mail_web = eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[{}]/div/label/input')".format(i))
                mail_web.send_keys(mail)
                print('Email Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Email in Web Retry','-'*10,i)
                i+=1
                time.sleep(2)

        while not link:
            try:
                full_name_web =eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[{}]/div/label/input')".format(i+1))
                full_name_web.send_keys(full_name)
                print('Full_name Successfully')
                break
            except NoSuchElementException:
                print('Cant Find Full_name in Web Retry','-'*10,i)
                i+=1
                time.sleep(2)

        while not link:
            try:
                user_web = eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[{}]/div/label/input')".format(i+2))
                user_web.send_keys(user)
                print('user_web Successfully')
                break
            except NoSuchElementException:
                print('Cant Find user_web in Web Retry','-'*10,i)
                i+=1
                time.sleep(2)


        while not link:
            try:
                password_web = eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[{}]/div/label/input')".format(i+3))
                password_web.send_keys(password)
                print('password_web Successfully')
                break
            except NoSuchElementException:
                print('Cant Find password_web in Web Retry','-'*10,i)
                i+=1
                time.sleep(2)
        # time.sleep(2)
        while not link:
            try:
                sign_up_btn=eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[{}]/div/button')".format(i+4))
                sign_up_btn.click()
                print('First Page Successfully')
                self.birthday()
                break
            except NoSuchElementException:
                print('Cant Find Sign up btn in Web Retry','-'*10,i)
                i+=1
                time.sleep(1)
                
                if i >10:

                    print('Email Name Eror')
                    eror=True
                    break
        if eror:
            ret,status=self.check_sign_up_eror(chek_parms)
            print('--Eror in Same User name Or mail--')

    def check_sign_up_eror(self,chek_parms):
        if chek_parms:

            time.sleep(2)

            user_eror = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/div/span')
            user_eror_out=user_eror.get_attribute("class")


            link = None
            i=0
            while not link:
                try:
                    user_eror =eval("self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[{}]/div/div/span')".format(i))
                    user_eror_out=user_eror.get_attribute("class")
                    print('Eror',user_eror_out)
                    # return False,'Eoror'
                    break
                except NoSuchElementException:
                    print('Cant Eror Retry','-'*10,i)
                    i+=1
                    time.sleep(2)

            print('out',user_eror_out[15:20])

            if user_eror_out[15:20] =='Error':
                print('out',user_eror_out[15:20])
                return False,'User Eror'

        else:
            return False,False


    def birthday(self):

        months=['January','February','March','April','May','June','July','August','September','October','November','December']
        month=random.randint(1,10)
        day=random.randint(2,29)
        year=random.randint(1980,1999)

        i=0
        link = None
        
        while not link:
            try:
                set_month=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select')
                set_month.send_keys(months[month])
                set_day=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select')
                set_day.send_keys(day)
                set_year=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
                set_year.send_keys(year)
                # sign_up_btn.click()
                time.sleep(1)
                noxt=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button')
                noxt.click()
                print('Page 2  Successfully')
                break
            except NoSuchElementException:
                print('Eror in page 2 Retry','-'*10,i)
                i+=1
                time.sleep(1)
                if i>10:
                    break

    def final_step(self,code):

        i=0
        link = None

        time.sleep(10)
        
        while not link:
            try:
                confirm_code=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')
                confirm_code.send_keys(code)
                time.sleep(1)
                change_mail=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
                change_mail.click()
                break
            except NoSuchElementException:
                print('Eror in page 2 Retry','-'*10,i)
                i+=1
                time.sleep(1)
                if i>10:
                    break




if __name__=='__main__':


    

    email_sites=['https://tempmailo.com/','https://temp-mail.org/en/','https://mail.tm/en/']
    selected_site=2
    email_site=email_sites[selected_site]

    conn_mail=connection()

    conn_mail.set_init()
    conn_mail.get_url(email_site)

    if email_site=='https://tempmailo.com/':

        email=conn_mail.get_email_address(email_site)
        print('email',email)
    elif email_site=='https://mail.tm/en/':

        email=conn_mail.get_email_mail_tm()


    # if email_site=='https://temp-mail.org/en/':
    #     email=conn_mail.get_email_address(email_site)


    conn_insta=connection()
    conn_insta.set_init()
    insta_signup_url='https://www.instagram.com/accounts/emailsignup/?hl=en'
    conn_insta.get_url(insta_signup_url)
    conn_insta.set_insta_parms(email,'milad','milad231231243423324','milad123456')





    # conn_mail.confirm_email()
        # conn.change_email()
    code=conn_mail.confirm_temp_mail()
    print('Confirm Code:',code)

    conn_insta.final_step(code)


    # /html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]


    # conn.get_email_address(email_site)
    # conn.change_email()

    # conn.get_email_address(email_site)
    # conn.change_email()

