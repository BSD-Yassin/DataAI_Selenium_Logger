"""
This is the selenium configuration loading. It depends on back.py for every tweak from the actual Undetected module.
In order, the module calls for every config file, proxy and user before launching an instance for undetected module.
This module then runs the simple login by XPATH. It detects if a captcha is required and calls for captcha_resolve from the captcha.py
"""

import time
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from solveRecaptcha import solveRecaptcha
from src.back import Configuration
from src.back import custom_ChromeOptions

class Uc_instance():
    def __init__(self):
        
        self.logger = Configuration.get_log()
        self.configuration = Configuration.config_loader()
        self.user = Configuration.users_loader()
        self.options = custom_ChromeOptions()
        self.driver = uc.Chrome(options=self.options, driver_executable_path='driver/chromedriver')

    def session_uc(self):
        try:
            print("Launching the browser...")
            self.driver.get('https://www.data.ai/account/login')
        except:
            self.logger.error(f'{time.asctime(time.localtime(time.time()))} - Something went wrong during the UcLaunch generation.')
            print('Something went wrong while loading the website')


    def xpath_logger(self):
        
        try:
            login_PATH = "/html/body/div[2]/div/div/div[1]/div/div[3]/form/div/div[1]/input"
            password_PATH = "/html/body/div[2]/div/div/div[1]/div/div[3]/form/div/div[2]/input"
            button_login = "/html/body/div[2]/div/div/div[1]/div/div[3]/form/div/button"
            get_started_button = '/html/body/div[2]/div/div/div[1]/div[1]/div[3]/div/button/span'

            self.driver.find_element(By.XPATH, login_PATH).send_keys(self.user['username'])
            self.driver.find_element(By.XPATH, password_PATH).send_keys(self.user['password'])
            self.driver.find_element(By.XPATH,button_login).click()
            
            test_log = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, get_started_button)))
            if test_log:
                print('Managed to log in ! No captcha !')
        except:
            self.logger.error(f'{time.asctime(time.localtime(time.time()))} - Error - Something went wrong while trying to login. - Actual page is {self.driver.current_url} - Login used is {self.user["username"]}')
            print('Something went wrong while trying to log in. Check log for more details.')
    
        
"""     def solver():
        result = solveRecaptcha(
            "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
            driver.current_url)

        code = result['code']

        print(code)

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'g-recaptcha-response')))

        browser.execute_script(
            "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")

        browser.find_element(By.ID, "recaptcha-demo-submit").click()

        time.sleep(120) """