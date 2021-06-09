import time
from selenium import webdriver


url = 'https://www.google.com/maps/place/%D0%9E%D0%B0%D0%B7%D0%B8%D1%81/@55.8029471,49.0908432,13z/data=!4m10!1m3!2m2!1z0JrQsNC30LDQvdGMINGB0YPQstC10L3QuNGA0Ys!6e6!3m5!1s0x415ead532abb0673:0xde6d1e23530868b1!8m2!3d55.826235!4d49.1005619!15sCh3QmtCw0LfQsNC90Ywg0YHRg9Cy0LXQvdC40YDRi1ofIh3QutCw0LfQsNC90Ywg0YHRg9Cy0LXQvdC40YDRi5IBDWdyb2Nlcnlfc3RvcmU?hl=ru-RU'
driver = webdriver.Firefox()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20)
driver.get(url)
time.sleep(3)
site = driver.find_element_by_css_selector('.HY5zDd')

print(site.text)

driver.quit()
# <div jstcache="319" class="QSFF4-text gm2-body-2" jsan="7.QSFF4-text,7.gm2-body-2">oasiscatalog.com</div>