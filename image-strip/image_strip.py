import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'machine',
  'password': 'learning',
  'host': '127.0.0.1',
  'database': 'LandmarkDB',
  'raise_on_warnings': True,
}

try:
    db = connection.MySQLConnection(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    db.close()
