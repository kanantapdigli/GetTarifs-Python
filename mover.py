import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time
import sys

url = "https://mover.az/az/CalcPrice"

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
    wait.until(presence_of_all_elements_located((By.CLASS_NAME, "tarifler")))
    weights = driver.find_elements_by_css_selector(".weight")
    prices = driver.find_elements_by_css_selector(".tarifler .col-lg-2 span:not(.country-name)")
    countries = driver.find_elements_by_css_selector(".tarifler .country-name")
    isKgList = []
    domainName = re.search('https?://([A-Za-z_0-9.-]+).*',url).group(1)

    for price in prices:
        if str(price.text).__contains__("kq"):
            is_per_kg = True
        else:
            is_per_kg = False

        isKgList.append(is_per_kg)

    prices_ = []
    for weight,price,is_per_kg in zip(weights,prices,isKgList):

        weight_ = str(weight.text)
        weight_number = re.findall(r'[-+]?\d*[.,]\d+|\d+', weight_)

        for country in countries:
            if len(weight_number) == 1:
                object = {"from": "0", "to": weight_number[0], "price": price.text, "maye": "false", "country": country.text,
                      "is_per_kg": str(bool(is_per_kg)), "source": domainName}
            elif len(weight_number) == 0:
                object = {"for": "Korporativ daşınmalar üçün", "to": "corporate@mover.az ünvanına mail yaza bilərsiniz", "country": country.text, "source": domainName}
            else:
                object = {"from": weight_number[0], "to": weight_number[1], "price": price.text, "maye": "false",
                          "country": country.text,
                          "is_per_kg": str(bool(is_per_kg)), "source": domainName}
            prices_.append(object)

for price in prices_:
    print(price)
    print()