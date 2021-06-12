import time
import re
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
    browser = webdriver.Firefox()

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
                print(len(list_urls))
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

def save_writer(all_data):
    with open('output.txt', 'a', encoding='utf-8', errors='ignore') as file:
        file.write(all_data + '\n')


def get_html_site(list_urls):
    for row_url in list_urls:
        if 'http' in row_url:
            try:
                driver = webdriver.Firefox()
                driver.maximize_window()  # For maximizing window
                driver.implicitly_wait(10)
                driver.get(row_url)
                time.sleep(3)
            except Exception as e:
                print('get_html_site', e)
                driver.close()
                driver.quit()
            try:
                all_data = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div')
            except Exception:
                all_data = 'organization'
            try:
                name_org = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
            except Exception:
                name_org = 'name org'
            # try:
            #     site = driver.find_element_by_css_selector(
            #         'div.RcCsl:nth-child(5) > button:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text
            # except Exception:
            #     site = 'site'
            # try:
            #     name_org = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]')
            #     row_tag = str(name_org.get_attribute('innerHTML'))
            #     telephone = re.findall(r"\d\(\d{3}\)\d{3}.\d{2}.\d{2}", row_tag)
            # except Exception:
            #     telephone = 'phone'

            print(all_data.text)
            save_writer(all_data.text)
            driver.quit()
        else:
            continue


def main():
    try:
        get_html_site(run_browser(get_town_in_file(), get_categories_in_file()))

    except KeyboardInterrupt:
        browser.quit()
    except Exception as e:
        print('main', e)


if __name__ == '__main__':
    main()
