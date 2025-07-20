from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By



# Set Firefox binary path manually
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Update if needed

# # Set the path to geckodriver
# serv_obj = Service(r"C:\browsers\geckodriver.exe")
# driver = webdriver.Firefox(service=serv_obj, options=options)
# import time

# # driver.get("https://www.google.com/")
# # driver.find_element(By.ID,"APjFqb").send_keys("cats")
# # driver.find_element(By.NAME,"btnK").click()

# driver.get("https://www.flipkart.com/")
# driver.maximize_window()


# search=driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
# search.send_keys("mobile phones")
# search.submit()
# time.sleep(5)
# driver.find_element(By.LINK_TEXT,"vivo T4x 5G (Marine Blue, 128 GB").click()
# time.sleep(3)
# cart=driver.find_element(By.XPATH,"//button[contains(text(), 'Add to cart')]")

# cart.click()

from selenium import webdriver
driver = webdriver.Firefox()

 driver.get("https://www.google.com/")

 driver.find_element(By.ID,"APjFqb").send_keys("cats")
 driver.find_element(By.NAME,"btnK").click()




