import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.mytinytodo.net/demo/#list/1")

action = ActionChains(driver)
driver.find_element(By.CSS_SELECTOR,"#task").send_keys("new_task")
driver.find_element(By.CSS_SELECTOR,"#newtask_submit").click()
time.sleep(3)
task_list = driver.find_elements(By.CSS_SELECTOR, "#tasklist>li")
for task in task_list:
    title_label = task.find_element(By.CSS_SELECTOR, ".task-title")
    if "new_task" in title_label.text:
        print(title_label.text)
        action.move_to_element(title_label).perform()
        task.find_element(By.CSS_SELECTOR, ".taskactionbtn").click()
        driver.find_element(By.CSS_SELECTOR, "#cmenu_delete").click()
        driver.find_element(By.CSS_SELECTOR, "#btnModalOk").click()



input("wwe")