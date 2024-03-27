#pip3 install -U selenium
#pip3 install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://admin-icta.nitb.gov.pk/login')
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('shehryarak@gmail.com')
pass_input = driver.find_element(By.NAME, 'password')
pass_input.send_keys('approver@123')
btn = driver.find_element(By.CLASS_NAME, 'btn-sign-in')
btn.click()
driver.get('https://admin-icta.nitb.gov.pk/domicile/applications')
a = 0
for span in driver.find_elements(By.TAG_NAME, 'span'):
    if len(span.text) !=0:
        a = a + 1
        if a == 1 and span.text == 'Sheryar Arif Khan':
            print('Loged In')
            break
for link in driver.find_elements(By.CLASS_NAME, 'btn-circle'):
    link.click()
