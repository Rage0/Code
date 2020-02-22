from Function_Parser import *

res = requests.get('https://www.google.ru')

if res.status_code == 200:
    print('<'*6 + 'Connect' + 6*'>')

    page = 0
    titleName = []
    titlePrice = []
    title = []
    while page != page_data():
        page += 1
        URL = 'https://ru.banggood.com/Wholesale-Electronics-c-1091-0-1-1-36-0_page{}.html'.format(page)

        for elem in parser(URL):
            names = elem.find('span', class_='title')
            price = elem.find('span', class_='wh_cn')
            titleName.append(names.getText().replace('\xa0', ' '))
            titlePrice.append(price.getText())
        print('<'*6, page, 6*'>')


    title.append(titleName)
    title.append(titlePrice)

    print(title)
    write_excel(title)

elif res.status_code == 404:
    print('<'*6 + 'Not connect' + 6*'>')
