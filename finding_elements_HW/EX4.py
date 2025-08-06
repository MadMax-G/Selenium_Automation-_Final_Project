import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#driver.get("https://whatismyipaddress.com/")

#IP = driver.find_element(By.CSS_SELECTOR, "#ipv6").text
#print(IP)
IP = "2a06:c701:95a9:4600:3cf3:271e:8a38:6f2f"

driver.get("https://apps.db.ripe.net/db-web-ui/query")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#queryStringInput").send_keys(IP)
driver.find_element(By.CSS_SELECTOR, ".mat-icon.notranslate.fal.fa-search.material-icons.mat-ligature-font.mat-icon-no-color").click()

# Получаем все блоки .resultpane — в каждом из них потенциально есть нужные данные
resultpanes = driver.find_elements(By.CSS_SELECTOR, "div.resultpane")

for pane in resultpanes:
    # Проверяем, есть ли внутри текст route6
    if "route6" in pane.text:
        # Нашли нужный блок, теперь внутри него ищем .whois-object-viewer
        viewer = pane.find_element(By.CSS_SELECTOR, ".whois-object-viewer")

        # Достаём все строки
        items = viewer.find_elements(By.CSS_SELECTOR, "li.ng-star-inserted")
        print("--- route6 ---")
        for item in items:
            print(item.text)
        break  # если нужен только один блок — выходим

input("wwe")