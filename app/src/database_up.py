from mysql.connector import connect, Error
import datetime
from src.back import Configuration

class DB_connect():
    def __init__(self):
        self.logger = Configuration.get_log()
        self.db_configuration = Configuration.db_loader()

    def mySQL_login(self):
        
        try :
            db_configuration = dict(self.db_configuration) 
        except :
            self.logger.error(f'{time.asctime(time.localtime(time.time()))} - Something went wrong during the DB configuration.')

        print(dict(db_configuration))
        try:
            with connect(
                host=db_configuration['host'],
                port=db_configuration['port'],
                database=db_configuration['database'],
                user=db_configuration['user'],
                password=db_configuration['password'],
            ) as connection:
                print(connection)
        except Error as e:
            self.logger.error(f'{time.asctime(time.localtime(time.time()))} - Something went wrong during the DB authentification.')
    
    def write_db(username, proxy_ip, success):
        """
        check if field "failed" is not NULL
        """

        time = datetime.datetime.now()
        dt = time.strftime("%Y-%m-%d %H:%M:%S")
        username = username
        proxy_ip = proxy_ip
        success = success
        add_login_time = ("INSERT INTO dataai_accounts "
               "(user, success, proxy_ip,  last_time) "
               "VALUES (%s, %s, %s, %s)")