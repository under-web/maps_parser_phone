import time
from selenium import webdriver


url = 'https://www.google.com/maps/search/Казань+сувениры/@55.802957,49.0908432,13z/data=!3m1!4b1?hl=ru-RU'
driver = webdriver.Firefox()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20)
driver.get(url)
time.sleep(3)
site = driver.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
for i in site:
    print(i.get_attribute('aria-label'))

print(site.text)

driver.quit()
# <a aria-label="Сувениры" jsaction="pane.wfvdle5;focus:pane.wfvdle5;blur:pane.wfvdle5;auxclick:pane.wfvdle5;contextmenu:pane.wfvdle5;keydown:pane.wfvdle5;clickmod:pane.wfvdle5" jstcache="127" href="https://www.google.com/maps/place/%D0%A1%D1%83%D0%B2%D0%B5%D0%BD%D0%B8%D1%80%D1%8B/data=!4m5!3m4!1s0x415ead1060310785:0xd8da41046261f9e3!8m2!3d55.788186!4d49.1204689?authuser=0&amp;hl=ru&amp;rclk=1" class="a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd" jsan="7.a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd,0.aria-label,8.href,0.jsaction"></a>