from src import sel
from src import back
from src import database_loader
import time
import datetime
import sys
import os

if __name__ == '__main__':
    while True :
        instance = sel.Uc_instance()
        instance.session_uc()
        instance.xpath_logger()
        
        db_instance = database_loader.DB_connect()
        db_instance.mySQL_login()
        
        print(instance.success)
        
        db_instance.write_db(instance.user['username'],
                            instance.user['password'],
                            failed=instance.success)

