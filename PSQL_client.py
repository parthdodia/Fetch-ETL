import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime


class PSQL_client:

    def __init__(self, **args):
        # Initialize the PostgreSQL client with default values for connection parameters
        self.user = args.get('user', 'postgres')
        self.password = args.get('password', 'postgres')
        self.port = args.get('port', 5432)
        self.dbname = args.get('dbname', 'postgres')
        self.host = args.get('host', 'localhost')
        self.debug = args.get('debug', False)
        self.db_fields = ["user_id", "device_type", "masked_ip", "masked_device_id", "locale", "app_version", "create_date"]
        self.connection = psycopg2.connect(
            user=self.user,
            password=self.password,
            port=self.port,
            dbname=self.dbname,
            host=self.host
        )

    def connect(self):
        pass  


    def disconnect(self):
        self.connection.close()


    def run_query(self, query, params=None):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, params)
        
        # If the query is a SELECT statement, fetch the results
        if query.lstrip().upper().startswith('SELECT'):
            result = cursor.fetchall()
        else:
            # If the query is an INSERT, UPDATE, or DELETE, commit the changes
            self.connection.commit()
        
        cursor.close()
        
        return result if 'result' in locals() else None


    def add_data(self, data):
        query = """CREATE TABLE IF NOT EXISTS user_logins(
                user_id varchar(128),
                device_type varchar(32),
                masked_ip varchar(256),
                masked_device_id varchar(256),
                locale varchar(32), 
                app_version integer,
                create_date date
                );"""
        self.run_query(query)

        query = """INSERT INTO user_logins(user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
                VALUES (%s, %s, %s, %s, %s, %s, TO_DATE(%s,'YYYYMMDD'));"""

        user_id = data.get('user_id')
        device_type = data.get('device_type')
        masked_ip = data.get('masked_ip')
        masked_device_id = data.get('masked_device_id')
        locale = data.get('locale')
        app_version = data.get('app_version')

        # Check if all required data is present
        if all([user_id, device_type, masked_ip, masked_device_id, locale, app_version]):
            # Prepare the parameters for the INSERT query
            params = (user_id, device_type, masked_ip, masked_device_id, locale, str(app_version).replace(".", ""), str(datetime.today().strftime('%Y%m%d')))
            self.run_query(query, params)
        else:
            print("Error: Missing data in the response")       
        self.connection.commit()


    def drop_table(self):
        query= """DROP TABLE IF EXISTS user_logins;"""
        self.run_query(query)