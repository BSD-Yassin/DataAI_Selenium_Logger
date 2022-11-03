"""
This is the selenium configuration loading. It depends on back.py for every tweak from the actual Undetected module.
In order, the module calls for every config file, proxy and user before launching an instance for undetected module.
This module then runs the simple login by XPATH. It detects if a captcha is required and calls for captcha_resolve from the captcha.py
"""
import time
import undetected_chromedriver as uc
from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from solveRecaptcha import solveRecaptcha
import socket
from src.back import Configuration
from src.back import custom_ChromeOptions

class Uc_instance():
    def __init__(self, success=False):
        
        self.logger = Configuration.get_log()
        self.configuration = Configuration.config_loader()
        self.user = Configuration.users_loader()
        self.options = custom_ChromeOptions()
        self.api = Configuration.get_api()
        # self.driver = webdriver.Remote(command_executor='http://172.17.0.2:4444', options=self.options, desired_capabilities=webdriver.DesiredCapabilities.CHROME)
        self.driver = uc.Chrome(options=self.options, driver_executable_path='driver/chromedriver')
        self.success = success
    
    def session_uc(self):
        try:
            print("Launching the browser...")
            self.driver.get('https://www.data.ai/account/login')
        except:
            failure = True
            return failure
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
                self.success = True
                print('Managed to log in ! No captcha !')
        except:
            self.logger.error(f'{time.asctime(time.localtime(time.time()))} - Error - Something went wrong while trying to login. - Actual page is {self.driver.current_url} - Login used is {self.user["username"]}')
            print('Something went wrong while trying to log in. Check log for more details.')
    
        
        def solver():

            import requests
            from time import sleep, time
            start_time = time()
            
            # send credentials to the service to solve captcha
            # returns service's captcha_id of captcha to be solved
            url="http://2captcha.com/in.php?key=1069c3052adead147d1736d7802fabe2&method=userrecaptcha&googlekey=6Lf5CQkTAAAAAKA-kgNm9mV6sgqpGmRmRMFJYMz8&pageurl=http://testing-ground.scraping.pro/recaptcha"
            resp = requests.get(url)

            if resp.text[0:2] != 'OK':
                quit('Error. Captcha is not received')
                captcha_id = resp.text[3:]
            
            # fetch ready 'g-recaptcha-response' token for captcha_id  
            fetch_url = "http://2captcha.com/res.php?key=1069c3052adead147d1736d7802fabe2&action=get&id=" + captcha_id
            for i in range(1, 20):
                sleep(5) # wait 5 sec.
                resp = requests.get(fetch_url)
                if resp.text[0:2] == 'OK':
                    break
                print('Time to solve: ', time() - start_time)
            
            # final submitting of form (POST) with 'g-recaptcha-response' token
            submit_url = "http://testing-ground.scraping.pro/recaptcha"
                # spoof user agent
            headers = {'user-agent': 'Mozilla/5.0 Chrome/52.0.2743.116 Safari/537.36'}
                # POST parameters, might be more, depending on form content
            payload = {'submit': 'submit', 'g-recaptcha-response': resp.text[3:]  }
            resp = requests.post(submit_url, headers=headers, data=payload)