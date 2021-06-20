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
    :return: список ссылок
    """
    global browser
    opts = Options()
    opts.headless = True
    assert opts.headless
    browser = webdriver.Firefox(options=opts)
    # browser = webdriver.Firefox()

    base_url = 'https://www.google.com/maps/search/' + town + '+' + categories + '/@55.802957,49.0908432,13z/data=!3m1!4b1?hl=ru-RU'
    browser.get(base_url)
    time.sleep(7)

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
                print(f'Найдено организаций {len(list_urls)} ')
        except Exception as e:
            print('2', e)
        time.sleep(3)
        try:
            button_next = browser.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]')
            button_next.click()
            time.sleep(3)
        except Exception as e:
            print('3', e)
            browser.close()
            browser.quit()
            return list_urls
        browser.close()
        browser.quit()
        return list_urls


def save_in_csv(out_data):
    with open("classmates.csv", mode="a", encoding='utf-8') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=";")
        file_writer.writerow(out_data)


#
# def save_writer(nam):
#     name_file = get_town_in_file() + '.txt'
#     with open(f'{name_file}', 'a', encoding='utf-8', errors='ignore') as file:
#         file.write(nam + '\n\n' + '-----------------------------------------------------------' + '\n\n')


def get_html_site(list_urls):
    for row_url in list_urls:
        if 'http' in row_url:
            try:
                opts = Options()
                opts.headless = True
                assert opts.headless
                driver = webdriver.Firefox(options=opts)
                # driver = webdriver.Firefox()
                driver.get(row_url)
                time.sleep(9)
            except Exception as e:
                print(e)
                continue
            try:
                main_info = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]').text

                main_info_dubler = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]').text
                name_org = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text

                row_phone = re.findall(r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})", main_info)
                row_phone2 = re.findall(r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})", main_info_dubler)
                site = re.findall(r'.+\.[a-zA-Z]{2,4}', main_info)
                site2 = re.findall(r'.+\.[a-zA-Z]{2,4}', main_info_dubler)
                #
                # phone = str(''.join(row_phone)) + str(''.join(row_phone2))
                # url0 = str(''.join(site)) + str(''.join(site2))

                # if not phone:
                #     phone = 'Телефон Не указан'
                # elif not url0:
                #     url0 = 'Сайт не указан'

                print('------------------------------------------------')
                print(f'Название " {name_org} "' + '\n')
                print(main_info)
                print(main_info_dubler)
                print('tel', row_phone)
                print('site  ', site)
                print('------------------------------------------------')
                print('')

                out_list = [name_org, row_phone, site]
                save_in_csv(out_list)

                driver.quit()

            except Exception as e:
                print('007', e)
                driver.close()
                driver.quit()
                continue
        else:
            continue


def main():
    print('Это бета-версия 1.1')
    print('Я работаю')
    try:
        get_html_site(run_browser(get_town_in_file(), get_categories_in_file()))

    except KeyboardInterrupt:
        browser.quit()
    except Exception as e:
        print('main', e)


if __name__ == '__main__':
    main()
# <h1 jstcache="127" class="x3AX1-LfntMc-header-title-title gm2-headline-5" jsan="7.x3AX1-LfntMc-header-title-title,7.gm2-headline-5"> <span jstcache="128">Лавка странника</span> <span jstcache="129" class="x3AX1-LfntMc-header-title-haAclf"></span> </h1>
