import time
from os import wait3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ebay.com/sch/ebayadvsearch")

driver.find_element(By.CSS_SELECTOR, "#_nkw").send_keys("guitar")
time.sleep(1)
dd = driver.find_element(By.CSS_SELECTOR, ".field.adv-field___sacat .field .select select")
dd = Select(dd)
dd.select_by_visible_text("Musical Instruments & Gear")
time.sleep(1)

label_list = driver.find_elements(By.CSS_SELECTOR, ".ui-range__entry .textbox__control")
label_list[0].send_keys("50")
label_list[1].send_keys("60")
time.sleep(1)

format_list = driver.find_elements(By.CSS_SELECTOR, ".adv-fieldset__format .field .field__label--end")
for i in format_list:
    print(i.text)
    if i.text == "Auction":
        i.click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".adv-form__actions .btn.btn--primary").click()
time.sleep(1)

input("wwe")