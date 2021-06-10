import time
from selenium import webdriver


url = 'https://www.google.com/maps/place/%D0%A5%D0%BE%D1%87%D1%83+%D0%98+%D0%92%D1%81%D0%B5!+%D0%9C%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD+%D0%9E%D1%80%D0%B8%D0%B3%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85+%D0%9F%D0%BE%D0%B4%D0%B0%D1%80%D0%BA%D0%BE%D0%B2/@55.7935526,49.1144165,13z/data=!3m1!5s0x415ead717f276ca9:0xfcf219537095334c!4m9!1m2!2m1!1z0JrQsNC30LDQvdGMINGB0YPQstC10L3QuNGA0Ys!3m5!1s0x415ead718497f4b7:0x6862f4f60c1123d9!8m2!3d55.7935526!4d49.1494354!15sCh3QmtCw0LfQsNC90Ywg0YHRg9Cy0LXQvdC40YDRi1ofIh3QutCw0LfQsNC90Ywg0YHRg9Cy0LXQvdC40YDRi5IBCWdpZnRfc2hvcA?hl=ru-RU'
driver = webdriver.Firefox()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20)
driver.get(url)
time.sleep(3)
name_org = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
adress = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]/div[1]/button/div[1]/div[2]/div[1]')
site = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[2]/div[1]')
phone = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]/div[4]/button/div[1]/div[2]/div[1]')
print(name_org.get_attribute("innerHTML"), phone.get_attribute("innerHTML"), site.get_attribute("innerHTML"), adress.get_attribute("innerHTML"))



driver.quit()
# <div jstcache="998" class="QSFF4-text gm2-body-2" jsan="7.QSFF4-text,7.gm2-body-2">8 (843) 253-71-09</div>