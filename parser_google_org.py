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
        return town


def get_categories_in_file():
    """
    Функция для извлечения категории из файла
    :return:  строка с категорией
    """
    with open('categories.txt', 'r', encoding='utf-8') as catg_town:
        categories = catg_town.read()
        return categories


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
        # browser.close()
        browser.quit()
        return list_urls


def save_writer(nam):
    name_file = get_town_in_file() + '.txt'
    with open(f'{name_file}', 'a', encoding='utf-8', errors='ignore') as file:
        file.write(nam + '\n\n' + '-----------------------------------------------------------' + '\n\n')


def get_html_site(list_urls):
    for row_url in list_urls:
        if 'http' in row_url:
            try:
                opts = Options()
                opts.headless = True
                assert opts.headless
                driver = webdriver.Firefox(options=opts)
                driver.get(row_url)
                time.sleep(7)
            except Exception as e:
                print(e)
                continue
            try:
                nam = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]')
                # adress = driver.find_element_by_xpath(
                #     '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
                print('------------------------------------------------')
                print(nam.text)
                print('------------------------------------------------')
                print('')
                save_writer(nam.text)
                driver.quit()
            except Exception as e:
                print('nam', e)
                driver.quit()
                continue
        else:
            continue


def main():
    print('Это бета-версия 1.0')
    print('Я работаю')
    try:
        get_html_site(run_browser(get_town_in_file(), get_categories_in_file()))

    except KeyboardInterrupt:
        browser.quit()
    except Exception as e:
        print('main', e)


if __name__ == '__main__':
    main()
