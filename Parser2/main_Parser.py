import requests
from bs4 import BeautifulSoup
from random import choice
from Proxy import proxies

useragents = open('useragents.txt').read().split('\n')
proxy = proxies()

for i in range(0, 5):
    user = {'user-agent': choice(useragents), 'accept': ''}

res = requests.get('https://www.google.ru')

if res.status_code == 200:
    print('<'*6 + 'Connect' + 6*'>')

    def get_html(url):
        r = requests.get(url, headers=user, proxies=proxy, timeout=5)
        r.encoding = 'utf8'
        return r.text


    def get_soup(url):
        soup = BeautifulSoup(url, 'html.parser')
        print(soup)
        return soup


    def parser(url):
        soup = get_soup(get_html(url))
        elems = soup.find_all('div', class_='main')
        return elems



    title = []
    URL = 'https://ru.banggood.com/Wholesale-3D-Printer-c-3480.html?akmClientCountry=Russian&from=nav'
    for elem in parser(URL):
        names = elem.find('span', class_='title')
        price = elem.find('span', class_='wh_cn')
        title.append(names.getText())
        title.append(price.getText())


    print(title)

elif res.status_code == 404:
    print('<'*6 + 'Not connect' + 6*'>')