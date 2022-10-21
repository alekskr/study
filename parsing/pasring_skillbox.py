import requests
from bs4 import BeautifulSoup

"Поиск заголовков и ссылок всех вебинаров"
req = requests.get('https://live.skillbox.ru/')
soup = BeautifulSoup(req.content, 'html.parser')
title = soup.title.text


name_link = {}
info = soup.findAll(class_="webinars__item")
for i in info:
    name = i.find(class_='webinar-card__title')
    link = i.find('a').get('href')
    name_link[name.text.strip()] = 'https://live.skillbox.ru/' + link
    # print('---------------------------------------')
    # print(name.text.strip())
    # print('https://live.skillbox.ru/' + link)

count = 1
for name, link in name_link.items():
    print(f'{count}. {name}: {link}')
    count += 1