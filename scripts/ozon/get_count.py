import time
import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = 'C:\\Users\\El1syum\\PycharmProjects\\ozon\\selenium\\chromedriver.exe'


def get_ozon_count(query):
    url = f'https://www.ozon.ru/search/?text={query}&from_global=true'
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    try:
        driver.get(url)
        time.sleep(1)
        try:
            count = driver.find_element(by=By.CLASS_NAME, value='taa4').text.split('найден')[1].split('товар')[0][
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
    ...
