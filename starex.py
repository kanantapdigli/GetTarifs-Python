import re
import requests

response = requests.get('https://starex.az/tariffs')

if response.ok:
    prices = re.search('var prices(.*?);', response.text, flags=re.S).group(0)

    domainName = re.search('https?://([A-Za-z_0-9.-]+).*', response.url).group(1)

    add_source = "source: " + repr(domainName) + " "

    startFrom = 0
    while startFrom < len(prices):
        index = prices.find("}", startFrom , len(prices))
        if index != -1:
            prices = prices[ : index] + add_source + prices[index : ]
            startFrom = index + len(add_source) +1
        else:
            break
else:
    print("Bad Request")

print(prices)


