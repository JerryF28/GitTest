import requests
from bs4 import BeautifulSoup as bs

print("Hello, World!\n")

def strToFloat(x):
    y = ""
    for i in x:
        if (i != ','):
            y += i
        else:
            y += '.'
    return float(y)

r = requests.get("https://yandex.ru/")

html = bs(r.content, 'html.parser')

convert = html.find_all("span", {"class" : "inline-stocks__value_inner"})

price = {"USD" : strToFloat(convert[0].text) , 
         "EUR" : strToFloat(convert[1].text) , 
         "OIL" : strToFloat(convert[2].text)
         }

for k, v in price.items():
    print(k, ':', v)

print("\nBye, World!\n")

print('evfefvevefve')