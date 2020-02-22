import requests
from bs4 import BeautifulSoup
from random import choice
from Proxy import proxies
import xlsxwriter
from time import sleep


def get_html(url):
    r = requests.get(url, headers=user, proxies=proxy)
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


def page_data():
    sleep(1)
    url = 'https://ru.banggood.com/Wholesale-Electronics-c-1091-0-1-1-36-0_page2.html'
    soup = get_soup(get_html(url))
    elems = soup.find('div', class_='page_num').find_all_next('a')[6].getText()
    return str(elems)


def write_excel(array):
    workbook = xlsxwriter.Workbook('Banggood.xlsx ')
    worksheet = workbook.add_worksheet()

    worksheet.write_column('A1', array[0]) # В колонну эксель
    worksheet.write_column('B1', array[1])

    workbook.close()

useragents = open('useragents.txt').read().split('\n')
proxy = proxies()


for i in range(0, 5):
    user = {'user-agent': choice(useragents), 'accept': ''}