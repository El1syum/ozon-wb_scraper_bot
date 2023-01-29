import logging

import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wildberries.ru',
    'Referer': 'https://www.wildberries.ru/catalog/obuv/muzhskaya/kedy-i-krossovki',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_wb_count(query):
    url = f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&lang=ru&locale=ru&pricemarginCoeff=1.0&query={query}&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&resultset=filters&spp=0&suppressSpellcheck=false'
    r = requests.get(url, headers=headers)
    try:
        data = r.json()
        total = data.get('data').get('total')
    except Exception as e:
        total = 'Возникла ошибка!'
        logging.error(f'[WB ERROR] {e}')
    return total


if __name__ == '__main__':
    ...
