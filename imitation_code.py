import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = ''
driver = webdriver.Firefox()
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(20)
driver.get(url)
time.sleep(3)
try:
    html = driver.find_element_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
    for i in range(5):
        html.send_keys(Keys.END)
        time.sleep(3)
except Exception as e:
    print('1', e)
name_org = driver.find_elements_by_class_name('ZY2y6b-RWgCYc')
nam = driver.find_elements_by_class_name('qBF1Pd-haAclf')
# adress = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]/div[1]/button/div[1]/div[2]/div[1]')
# site = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[2]/div[1]')
# phone = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[9]/div[4]/button/div[1]/div[2]/div[1]')
# print(name_org.get_attribute("innerHTML"), phone.get_attribute("innerHTML"), site.get_attribute("innerHTML"), adress.get_attribute("innerHTML"))
# row_tag = str(name_org.get_attribute('innerHTML'))
# telephone = re.findall(r"\d\(\d{3}\)\d{3}.\d{2}.\d{2}", row_tag)
main_page = driver.page_source

n = 0
for i in name_org:

    print(nam[n].text, '----+', i.text)
    print('_________________________________________________________')
    n += 1
# for j in name_org:
#     print(j.get_attribute('innerHTML').text)
print(main_page)
driver.quit()








