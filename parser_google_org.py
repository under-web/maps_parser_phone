# import selenium
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

list_urls = []


def get_town_in_file():
    with open('town.txt', 'r', encoding='utf-8') as file_town:
        town = file_town.read()
        return town


def get_categories_in_file():
    with open('categories.txt', 'r', encoding='utf-8') as catg_town:
        categories = catg_town.read()
        return categories


def run_browser(town, categories):
    global browser
    opts = Options()
    opts.headless = True
    assert opts.headless
    browser = webdriver.Firefox()

    base_url = 'https://www.google.com/maps/search/' + town + '+' + categories + '/@55.802957,49.0908432,13z/data=!3m1!4b1?hl=ru-RU'

    browser.get(base_url)
    time.sleep(7)
    while True:
        try:  # скроллим вниз в окне организаций до конца
            for i in range(6):
                html = browser.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]')
                html.send_keys(Keys.END)
                time.sleep(3)
        except Exception as e:
            if 'is not reachable by keyboard' in e:
                print('Не нашел элемент для зацепа')
            else:
                print(e)

        elems = browser.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            list_urls.append(elem.get_attribute("href"))
            print(len(list_urls))
        time.sleep(3)
        try:
            button_next = browser.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]')
            button_next.click()
        except Exception as e:
            if 'obscures it' in e:
                time.sleep(3)
                button_next = browser.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]')
                button_next.click()
            else:
                pass
def main():
    try:
        run_browser(get_town_in_file(), get_categories_in_file())
    except KeyboardInterrupt:
        browser.quit()
    except Exception as e:
        print(e)
        # browser.quit()


if __name__ == '__main__':
    main()
