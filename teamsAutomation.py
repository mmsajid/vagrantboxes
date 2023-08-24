from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium_stealth import stealth

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time  

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.implicitly_wait(15)

url = "https://teams.microsoft.com/_#/conversations/48:notes?ctx=chat"

try:
  
    driver.get(url)
    print("Page is ready!")

    srchElement = driver.find_element(By.ID,"control-input")
    actions = ActionChains(driver)
    actions.click(srchElement).send_keys("FirstName LastName").send_keys(Keys.ENTER).perform()
    time.sleep(3)

      # Switch to iframe
    iframe = driver.find_element(By.XPATH,"//iframe")
    driver.switch_to.frame(iframe)

    actions = ActionChains(driver)
    profilePicElement = driver.find_element(By.XPATH,"//h4[text()='People']/following::div[1]//img")
    actions.move_to_element(profilePicElement).perform()
    
    time.sleep(2)


    departmentName = driver.find_element(By.XPATH,"//div[@data-log-name='Department']").text
    print(departmentName)

    timeZone = driver.find_element(By.XPATH,"//*[name()='svg' and @aria-label='Clock']/following-sibling::p").text
    print(timeZone)
    
    print("Search is done!")
    print("Search is done!")
    print("Search is done!")

except Exception as e:
  print(e)
  print("Error")
finally:
  driver.close()
