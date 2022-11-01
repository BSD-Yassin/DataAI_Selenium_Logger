"""
This loads everything from the ini files, this also loads the logging for log files after loading the instance.
For now, only errors from the processes are thrown into the log file.
"""
import undetected_chromedriver as uc
import configparser
import logging 
from random import choice

class Configuration():
    def __init__(self):
        self.logger = logger
        self.proxy_creds = proxy_creds
        self.api_key = api_key
        self.current_user_dict = current_user_dict

    # One of the first thing to launch to write in the log
    def get_log():
        """
        Generates the log and prepares the logger for any error writing.
        """
        logger = logging.getLogger('mylogger')
        handler = logging.FileHandler('mylog.log')
        logger.addHandler(handler)
        return logger

    # Credentials reader
    def config_loader():
        """ 
        the api from the captcha solver 
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        api_key = dict(config.items('API_KEY'))
        return api_key

    ## Users_Loaders
    def users_loader():
        """
        loads every users from the users.ini file 
        """
        config = configparser.ConfigParser()
        config.read('users.ini')
        users = config.sections()
        
        current_user_choice = choice(users)
        current_user_dict = dict(config.items(current_user_choice))
        return current_user_dict
    
    def get_api():
        """
        loads the api key configuration
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        api_conf = config.items('API_KEY')
        return api_conf
        
    def db_loader():
        """
        loads the db configuration
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        database_conf = config.items('DATABASE')
        return database_conf
        
def custom_ChromeOptions():

    try : 
        config = configparser.ConfigParser()
        config.read('config.ini')
        proxy_creds = dict(config.items('PROXY'))    
        proxy = proxy_creds['proxy']

        print("Setting up the undetected session")
        options = uc.ChromeOptions()
        options.add_argument('--enable-javascript')
        options.add_argument("--disable-extensions")
        options.add_argument('--profile-directory=Default')
        options.add_argument("--incognito")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        # options.add_argument('--proxy-server=%s' % proxy)
        return options
        
    except :
        logging.error(f'{time.asctime(time.localtime(time.time()))} - Something went wrong during the ChromeOption generation.' + uc.ChromeOptions().arguments )
        print("Something went wrong in the ChromeOptions configuration")