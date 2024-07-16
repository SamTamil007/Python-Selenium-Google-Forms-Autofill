## Selenium Script Documentation for Automating Google Form Submission

### Overview
This Python script uses the Selenium library to automate the process of filling out and submitting a Google Form. It includes handling form fields such as name, contact number, email, address, pin code, date of birth, gender, and a dynamically generated verification code.

### Prerequisites
- **Selenium**: Ensure you have Selenium installed. You can install it using `pip install selenium`.
- **WebDriver**: Download the appropriate WebDriver (e.g., ChromeDriver for Chrome) and specify its path in the script.
- **Google Form URL**: The script is set to a specific Google Form URL that needs to be filled out.

### Steps

1. **Setup WebDriver**:
   ```python
   from selenium import webdriver
   from selenium.webdriver.common.keys import Keys
   from selenium.webdriver.common.by import By
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.chrome.service import Service
   from time import sleep

   driver_path = r'C:\path\to\your\chromedriver.exe'
   service = Service(driver_path)
   driver = webdriver.Chrome(service=service)
   ```

2. **Open the Google Form**:
   ```python
   form_url = 'https://forms.gle/WT68aV5UnPajeoSc8'
   driver.get(form_url)
   ```

3. **Wait for and Fill Out the Form Fields**:
   - **Full Name**:
     ```python
     wait = WebDriverWait(driver, 10)
     full_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
     full_name_field.send_keys('John Doe')
     ```

   - **Contact Number**:
     ```python
     contact_number_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
     contact_number_field.send_keys('1234567890')
     ```

   - **Email ID**:
     ```python
     email_id_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
     email_id_field.send_keys('john.doe@example.com')
     ```

   - **Full Address**:
     ```python
     full_address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
     full_address_field.send_keys('123 Main Street, City, Country')
     ```

   - **Pin Code**:
     ```python
     pin_code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
     pin_code_field.send_keys('123456')
     ```

   - **Date of Birth**:
     ```python
     dob_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
     dob_field.send_keys('01011990')  # Format: MMDDYYYY
     ```

   - **Gender**:
     ```python
     gender_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
     gender_field.send_keys('Male')
     ```

   - **Verification Code**:
     ```python
     verification_code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
     element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i30"]/span[1]/b')))  # Replace with your element's XPATH
     element_text = element.text
     verification_code_field.send_keys(element_text)
     ```

4. **Submit the Form**:
   ```python
   submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
   submit_button.click()
   print("Form submitted successfully.")
   ```

5. **Exception Handling and Cleanup**:
   ```python
   except Exception as e:
       print(f"An error occurred: {e}")
   finally:
       sleep(5)
       driver.quit()
   ```

### Explanation
- **WebDriver Setup**: Initializes the Chrome WebDriver with the path to the executable.
- **Form Navigation**: Opens the Google Form URL in the browser.
- **Field Interaction**: Uses `WebDriverWait` and `EC.presence_of_element_located` to ensure elements are available before interacting with them.
- **Exception Handling**: Catches any exceptions that occur during the process and prints an error message.
- **Cleanup**: Ensures the browser is closed after the script completes or if an error occurs, with a 5-second delay for viewing the result.

### Usage
This script is useful for automating repetitive form submission tasks. It can be modified to accommodate different form structures by updating the XPaths and field values accordingly.
