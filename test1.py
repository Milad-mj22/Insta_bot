import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

# tbb_dir = 'tor-browser-linux64-11.0.14_en-US/tor-browser_en-US/Browser/firefox'
# tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_dir)
# with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
#     driver.load_url("https://check.torproject.org")

# tor_process.kill()
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# profile = FirefoxProfile("tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default")
# profile.set_preference('network.proxy.type', 1)
# profile.set_preference('network.proxy.socks', '127.0.0.1')
# profile.set_preference('network.proxy.socks_port', 9050)

options = FirefoxOptions()
# options.profile = profile
binary = FirefoxBinary("'tor-browser-linux64-11.0.14_en-US/tor-browser_en-US/Browser/firefox'")

print ("0")
driver = webdriver.Firefox(options=options, firefox_binary=binary)
print ("1")
driver.get('https://check.torproject.org/')