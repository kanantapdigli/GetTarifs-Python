import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time
import sys

url = "https://expargo.com/pricing"

chrome_driver_path ="C:\\Users\\Kenan\\PycharmProjects\\getTarifs\\chromedriver.exe"

chrome_options = Options()

chrome_options.add_argument("--headless")

webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path,
    options= chrome_options
)

with webdriver as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    wait.until(presence_of_all_elements_located((By.CLASS_NAME, "card-body")))
    weights = driver.find_elements_by_css_selector(".text-right .text-primary")
    prices = driver.find_elements_by_css_selector(".text-primary.font-weight-bolder")
    states = driver.find_elements_by_class_name("cardhead")

    prices_ = []
    domainName = re.search('https?://([A-Za-z_0-9.-]+).*',url).group(1)

    for weight, price in zip(weights, prices):
        weight_ = str(weight.text)
        object = { "from": weight_[:4],"to": weight_[9:13],"price": price.text,"maye":"", "country": "TR", "is_per_kg": "false", "source":domainName}

        prices_.append(object)

for price in prices_:
    print(price)
    print()