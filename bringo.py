import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time
import sys

url = "https://bringo.az/tariff-list"

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
    wait.until(presence_of_all_elements_located((By.CLASS_NAME, "glyph")))
    weights = driver.find_elements_by_class_name("mls")
    prices = driver.find_elements_by_class_name("company-not-rated")
    domainName = re.search('https?://([A-Za-z_0-9.-]+).*', url).group(1)

    prices_ = []
    for weight, price in zip(weights, prices):
        weight_ = str(weight.text)
        object = {"from": weight_[:4], "to": weight_[11:15], "price": price.text, "maye": "false", "country": "AZ",
                  "is_per_kg": "false", "source": domainName}

        prices_.append(object)

for price in prices_:
    print(price)
    print()

