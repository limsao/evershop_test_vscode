from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

driver= webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))

driver.get( "http://localhost:3000/" )
driver.find_element(By.LINK_TEXT, "Classic Leather Loafers").click()


driver.find_element(By.CSS_SELECTOR, ".button.primary.outline").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".add-cart-popup-button").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".shopping-cart-checkout-btn.flex.justify-between.mt-8").find_element(By.CSS_SELECTOR, ".button.primary").click()
driver.find_element(By.NAME, "email" ).send_keys("client@mail.fr")
driver.find_element(By.CSS_SELECTOR, ".button.primary").click()
WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".checkout-payment.checkout-step"))
    )

# on rempli le form d e shipping
driver.find_element(By.NAME, "address[full_name]").send_keys("Nom prenom")
driver.find_element(By.NAME, "address[telephone]").send_keys("0607080911")
driver.find_element(By.NAME, "address[address_1]").send_keys("rue des fruits")
driver.find_element(By.NAME, "address[city]").send_keys("Charbo")
driver.find_element(By.NAME, "address[postcode]").send_keys("69999")
driver.find_element(By.NAME, "address[telephone]").send_keys("0607080911")
Select(driver.find_element(By.ID, "address[country]")).select_by_index(1)
Select(driver.find_element(By.ID, "address[province]")).select_by_index(1)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='e6970240-54c0-43f5-8b0f-ea3213735f75']").click()
#driver.find_element(By.CSS_SELECTOR, ".field-wrapper.radio-field").find_element(By.CSS_SELECTOR, ".method0").click()
time.sleep(12)
#driver.find_element(By.CSS_SELECTOR, ".form-submit-button.flex.border-t.border-divider.mt-4.pt-4").find_element(By.CSS_SELECTOR, ".button.primary").click()

#ckjbckjd
