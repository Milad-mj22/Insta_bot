# import from selenium
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os
from selenium import webdriver
import time

binary = 'tor-browser-linux64-11.0.14_en-US/tor-browser_en-US/Browser/firefox'
# the location of 
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

browser = None
def get_browser(binary=None,options=None):
    global browser  
    # only one instance of a browser opens, remove global for multiple instances
    if not browser: 
        browser = webdriver.Firefox(firefox_binary=binary)
    return browser

browser = get_browser(binary=firefox_binary)


# click on connect to connect the tor browser to the remote nodes
# browser.find_element_by_xpath('//*[@id="connectButton"]').click()
time.sleep(10)

# check my IP address
url='https://check.torproject.org/'
browser.get(url)