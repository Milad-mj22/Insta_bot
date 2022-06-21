from selenium import webdriver

from itertools import cycle

from seleniumwire import webdriver

profile = webdriver.FirefoxProfile() 

socks=["178.62.193.19","176.9.75.42","120.132.52.180"]

ports=[8080,3128,8888]

socks_ports={}

socks_ports=dict(zip(socks,ports))

socks_pool=cycle(socks_ports.keys())

ports_pool=cycle(socks_ports.values())

def ChangeProxy(ProxyHost,ProxyPort):

    options = {

    'proxy': {

        'http': 'http://username:password@'+str(ProxyHost)+':'+str(ProxyPort),

        'https': 'https://username:password@'+str(ProxyHost)+':'+str(ProxyPort),

        'no_proxy': 'localhost,127.0.0.1,dev_server:8080'

        }

    }

    return webdriver.Firefox(seleniumwire_options=options)

while True:

    socks_item=next(socks_pool)

    ports_item=next(ports_pool)

    print(type(socks_item))

    print(type(ports_item))


    try:
        driver=ChangeProxy(socks_item,ports_item)

        driver.get("https://www.ipchicken.com/")
    except:
        continue