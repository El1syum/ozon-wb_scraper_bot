import logging
import os
import pathlib
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

current_dir = pathlib.Path().resolve()

CHROME_DRIVER_PATH = os.path.join(current_dir, 'chromedriver')


def get_ozon_count(query):
    try:
        url = f'https://www.ozon.ru/search/?text={query}&from_global=true'
        s = Service(executable_path=CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
    except Exception as e:
        logging.error(f'SELENIUM DID NOT RUN\n{e}')
        return 'Возникла ошибка...'
    try:
        driver.get(url)
        time.sleep(1)
        try:
            count = driver.find_element(by=By.CLASS_NAME, value='a0ah').text.split('найден')[1].split('товар')[0][
                    1:].strip()
        except NoSuchElementException:
            count = f'По запросу {query} ничего не найдено...'
    except Exception as e:
        count = f'Возникла ошибка!'
        logging.error(f'[OZON ERROR] {e}')
    finally:
        driver.quit()

    return count


if __name__ == '__main__':
    print(get_ozon_count('кепки'))
