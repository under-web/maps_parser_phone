import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

list_urls = []

def get_town_in_file():
    """
     Функция для извлечения города из файла
    :return: строка с городом
    """
    with open('town.txt', 'r', encoding='utf-8') as file_town:
        town = file_town.read()
        return town.strip()


def get_categories_in_file():
    """
    Функция для извлечения категории из файла
    :return:  строка с категорией
    """
    with open('categories.txt', 'r', encoding='utf-8') as catg_town:
        categories = catg_town.read()
        return categories.strip()


def run_browser(town, categories):
    """
    Функция для сбора всех ссылок по запросу категории и города
    :param town: город для поиска берёт из файла
    :param categories: категория поиска берёт из файла
    :return: list() список ссылок
    """
    global browser
    opts = Options()
    opts.headless = True
    assert opts.headless
    browser = webdriver.Firefox(options=opts)
    # browser = webdriver.Firefox()

    print('Подгружаю...')

    base_url = 'https://www.google.com/maps/search/' + town + '+' + categories + '/@55.802957,49.0908432,13z/data=!3m1!4b1?hl=ru-RU'
    browser.get(base_url)
    time.sleep(7)

    count_page = 1  # счетчик страниц
    while True:
        # скроллим вниз в окне организаций до конца
        try:
            html = browser.find_element_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
            for i in range(5):
                html.send_keys(Keys.END)
                time.sleep(3)
        except Exception as e:
            print('1', e)

        try:
            elems = browser.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                list_urls.append(elem.get_attribute("href"))
            print(f' Страница {count_page} собрано {len(list_urls)} организаций.  ')
        except Exception as e:
            print('2', e)
        time.sleep(3)

        try:
            button_next = browser.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]')  # ищем кнопку жмем
            button_next.click()
            count_page += 1
            time.sleep(3)
        except Exception as e:
            if 'is not clickable' in str(e):
                print('Собираю данные')
                browser.close()
                browser.quit()
                return list_urls
            else:
                print(e)
                browser.close()
                browser.quit()
                return list_urls
        browser.close()
        browser.quit()
        return list_urls


def save_in_csv(town, out_data):
    """
    Функция для записи списка в файл CSV
    :param out_data: принимает список имя организации, телефон, сайт
    :return:
    """
    with open(f"{town}.csv", mode="a", encoding='utf-8') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=";")
        file_writer.writerow(out_data)

def get_html_site(list_urls):
    """
    Принимает список со всеми url, проходит по каждому адресу ищет данные и передает их в функцию записи
    :param list_urls: список с адресами
    :return:
    """

    for row_url in list_urls:
        if 'http' in row_url:
            try:
                opts = Options()
                opts.headless = True
                assert opts.headless
                driver = webdriver.Firefox(options=opts)  # загружаем браузер
                # driver = webdriver.Firefox()
                driver.get(row_url)
                time.sleep(9)
            except Exception as e:
                print(e)
                continue
            try:
                main_info = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]').text  # ищем элементы на страницы

                main_info_dubler = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]').text
                name_org = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text

                # TODO: не отображается потому что если номер main_info но regex не подходит он идет дальше, а твм []
                # row_phone = re.findall(r'[0-9]\s\(\d{0,4}\)\s\d{0,4}\-\d{0,3}\-\d{0,3}', main_info)
                amer_rus_regex = re.compile(r'\s\+\d.+')
                only_rus_regex = re.compile(r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})')
                any_regex = re.compile(r'\+\d.+')

                row_phone = re.findall(amer_rus_regex, main_info)
                row_phone2 = re.findall(only_rus_regex, main_info_dubler)
                row_phone3 = re.findall(any_regex, main_info_dubler)

                print('+++++++++++++++++++++++++')
                print('-|-', main_info, '-||-', main_info_dubler, '-|||-')
                print(f'row_phone {row_phone}', f'row_phone2 {row_phone2}')
                print(f'row_phone {row_phone3}')# Дебаг инфо
                print('++++++++++++++++++++++++++')


                if row_phone:
                    phone = ''.join(list(row_phone[0]))
                elif row_phone2:
                    phone = ''.join(list(row_phone[0]))
                elif row_phone3:
                    phone = ''.join(list(row_phone[0]))
                else:
                    phone = 'Не указан тел'


                row_site = re.findall(r'.+\.[a-zA-Z]{2,4}', main_info)
                row_site2 = re.findall(r'.+\.[a-zA-Z]{2,4}', main_info_dubler)

                if row_site != []:
                    site = ''.join(row_site)  # блок для поиска сайта
                elif row_site2 != []:
                    site = ''.join(row_site2)
                else:
                    site = 'Не указан сайт'

                print('------------------------------------------------')  # дебаг инфо
                print(f'Название " {name_org} "' + '\n')
                print(main_info)
                print(main_info_dubler)
                print('tel', phone)
                print('site  ', site)
                print('------------------------------------------------')
                print('')

                out_list = [name_org, phone, site]

                save_in_csv(get_town_in_file(), out_list)  # формируем список и передаем в ф-цию записи CSV

                driver.quit()

            except Exception as e:
                print('get_html_site err:', e)
                driver.close()
                driver.quit()
                continue
        else:
            continue


def main():
    print(' v3c.r stable')
    print('Запуск.')
    try:
        get_html_site(run_browser(get_town_in_file(), get_categories_in_file()))

    except KeyboardInterrupt:
        browser.close()
        browser.quit()
    except Exception as e:
        if 'neterror' in str(e):
            print('Проверьте интернет соединение')
            browser.close()
            browser.quit()
        else:
            print('main', e)
            browser.close()
            browser.quit()



if __name__ == '__main__':
    main()
