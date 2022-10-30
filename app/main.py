from src import sel
from src import back
from src import database_up
import time
import datetime
import sys
import os

if __name__ == '__main__':
    while True:
        instance = sel.Uc_instance()
        instance.session_uc()
        instance.xpath_logger()
        print('---  Logged with --' + instance.user['username'] + '--at--' + f'{datetime.datetime.now()}  ---')
        time.sleep(5)