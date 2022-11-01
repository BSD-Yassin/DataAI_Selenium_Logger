from mysql.connector import connect, Error
import datetime
import time
from src.back import Configuration

class DB_connect():
    def __init__(self):
        self.logger = Configuration.get_log()
        self.db_configuration = Configuration.db_loader()
        self.connection = self.mySQL_login()

    def mySQL_login(self):
        
        try :
            db_configuration = dict(self.db_configuration) 
        except :
            self.logger.error(f'{time.asctime(time.localtime(time.time()))} - Something went wrong during the DB configuration.')

        try:    
            connection = connect(
                host=db_configuration['host'],
                port=db_configuration['port'],
                database=db_configuration['database'],
                user=db_configuration['user'],
                password=db_configuration['password'])
            return connection
        
        except Error as e:
            self.logger.error(f'{time.asctime(time.localtime(time.time()))} - Something went wrong during the DB authentification.')
    
    def write_db(self, email, password, proxy_ip, failed):
        """
        Change values        
        """
        try :
            connection = self.connection 
            # time = datetime.datetime.now()
            # used = time.strftime("%Y-%m-%d %H:%M:%S")
            # sessionid = sessionid
            # proxy_ip = proxy_ip

            failed = failed
            with connection.cursor() as cursor: 
                query_add_login_time = """
                    UPDATE dataai_accounts SET failed=%s WHERE email=%s 
                    """ % (failed, email)
                connection.commit()
        except:
            self.logger.error(f'{time.asctime(time.localtime(time.time()))} - Something went wrong during the DB queries.')