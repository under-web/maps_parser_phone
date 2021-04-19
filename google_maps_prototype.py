import re
import time
import pyautogui

from selenium import webdriver
from bs4 import BeautifulSoup

# ----------------------------- #
#  Парсер телефонов из гуглмапс #
#  ____________________________ #



def get_phone(main_page):
    soup = BeautifulSoup(main_page, 'lxml')
    title = soup.find_all('span')
    list_phone = []
    # TODO: преобразователь номеров допилить
    result = re.findall(r'\d\s\(\d{3}\)\s\d{3}\-\d\d\-\d\d', str(title))
    for phone in result:
        list_phone.append(phone)
    print(len(set(list_phone)))
    print(list_phone)
    with open('result.txt', 'a', encoding='utf-8') as fl:
        for i in list_phone:
            fl.write(i + '\n')
    return print('Записано')


def main():
    driver = webdriver.Firefox()

    driver.get(
        'https://www.google.ru/maps/search/%D0%B4%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B5+%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7'
        '%D0%B8%D0%BD%D1%8B/@56.864356,53.0880159,11z/data=!3m1!4b1')
    time.sleep(10)
    while True:
        # print(pyautogui.position())
        pyautogui.moveTo(168, 242, 2)
        pyautogui.click()
        pyautogui.moveTo(136, 433, 2)
        time.sleep(3)
        pyautogui.scroll(-3000)
        time.sleep(2)
        pyautogui.scroll(-3000)
        time.sleep(5)
        main_page = driver.page_source


        get_phone(main_page)
        bottom = driver.find_element_by_xpath('//*[@id="n7lv7yjyC35__section-pagination-button-next"]/img')
        bottom.click()
        # time.sleep(7)


if __name__ == '__main__':
    main()
