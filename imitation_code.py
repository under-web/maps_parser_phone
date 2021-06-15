import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.google.ru/maps/place/%D0%A5%D0%BE%D1%87%D1%83+%D0%98+%D0%92%D1%81%D0%B5!+%D0%9C%D0%B0%D0%B3%D0%B0' \
      '%D0%B7%D0%B8%D0%BD+%D0%9E%D1%80%D0%B8%D0%B3%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85+%D0%9F%D0%BE%D0%B4' \
      '%D0%B0%D1%80%D0%BA%D0%BE%D0%B2/@55.8028705,49.0908432,' \
      '13z/data=!3m1!5s0x415ead717f276ca9:0xfcf219537095334c!4m9!1m2!2m1!1z0LrQsNC30LDQvdGMINGB0YPQstC10L3QuNGA0Ys' \
      '!3m5!1s0x415ead718497f4b7:0x6862f4f60c1123d9!8m2!3d55.7935526!4d49.1494354' \
      '!15sCh3QutCw0LfQsNC90Ywg0YHRg9Cy0LXQvdC40YDRi1ofIh3QutCw0LfQsNC90Ywg0YHRg9Cy0LXQvdC40YDRi5IBCWdpZnRfc2hvcA '
driver = webdriver.Firefox()
# driver.maximize_window()  # For maximizing window
# driver.implicitly_wait(20)
driver.get(url)
time.sleep(15)

nam = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]')
# adress = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').get_attribute('innerHTML')
print('------------------------------------------------')
print(nam.text)
print('------------------------------------------------')
print('')
print('')
# print(f'телефон  {telephone}')
driver.quit()

