import requests
from bs4 import BeautifulSoup
from random import choice
res = requests.get('https://google.com')

if res.status_code == 200:
    print('<<<<<<<<<<<<<<<<<<<Connect!>>>>>>>>>>>>>>>>>>>>>>')

    k = 0
    titleArray = []

    def get_html(url):
        r = requests.get(url)
        r.encoding = 'utf8'
        return r.text


    def get_soup(HTML):
        soup = BeautifulSoup(HTML, 'html.parser')
        print(soup)
        return soup


    def parserName(url):
        soup = get_soup(get_html(url))
        elems = soup.find('table', id='proxylisttable').find_all_next('tr')[1:12]
        return elems

    def proxies():
        URL = 'https://free-proxy-list.net'
        for proxy in parserName(URL):
            proxyFull = proxy.find_all('td')
            ip = proxyFull[0].getText()
            port = proxyFull[1].getText()
            ht = 'https' if 'yes' in proxyFull[6].getText() else 'http'
            title = {'schema': ht, 'address': ip + ':' + port}
            titleArray.append(title)
        return choice(titleArray)


elif res.status_code == 404:
    print('<<<<<<<<<<<<<<<<<<<Not found!>>>>>>>>>>>>>>>>>>>>>')