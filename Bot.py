import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Parametrage de Selenium
firefoxPath = r'C:\Program Files\Mozilla Firefox\firefox.exe'
option = webdriver.FirefoxOptions()
option.binary_location = firefoxPath

service = Service(GeckoDriverManager().install())
geckodriverPath = r'C:\Python27\Scripts\geckodriver.exe'

driver = webdriver.Firefox(service=service, options = option)
url = "https://www.leboncoin.fr/"
driver.get(url)