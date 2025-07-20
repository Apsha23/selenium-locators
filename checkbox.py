from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By



# Set Firefox binary path manually
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Update if needed

# Set the path to geckodriver
serv_obj = Service(r"C:\browsers\geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj, options=options)
import time

driver.get("https://practice.expandtesting.com/checkboxes")
box=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(box))

box1=driver.find_element(By.XPATH,"//input[@id='checkbox1']")
print(box1.is_enabled())
print(box1.is_displayed())
print(box1.is_selected())
box1.click()
print(box1.is_selected())

driver.quit()

for i in range(2):
    if i>=1:
        box[i].click()
        print(box[i].get_attribute('id'))

driver.quit()

for checkbox in box:
        checkbox.click()
        print(checkbox.get_attribute('id'))
driver.quit()

checkbox2=box[1]

for checkbox in box:
    if checkbox == checkbox2:
        checkbox.click()
        print(checkbox.get_attribute('id'))
driver.quit()






