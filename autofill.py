from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_path = r'C:\Users\Solom\Downloads\Compressed\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

form_url = 'https://forms.gle/WT68aV5UnPajeoSc8'  
driver.get(form_url)

try:
    
    wait = WebDriverWait(driver, 10)
    full_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    full_name_field.send_keys('John Doe')
    contact_number_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    contact_number_field.send_keys('1234567890')
    email_id_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_id_field.send_keys('john.doe@example.com')
    full_address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    full_address_field.send_keys('123 Main Street, City, Country')
    pin_code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pin_code_field.send_keys('123456')
    dob_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    dob_field.send_keys('01011990')  # Format: MMDDYYYY
    gender_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gender_field.send_keys('Male')
    verification_code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i30"]/span[1]/b')))  # Replace with your 
    element_text = element.text
    verification_code_field.send_keys(element_text)
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    print("Form submitted successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:

    sleep(5)
    driver.quit()
