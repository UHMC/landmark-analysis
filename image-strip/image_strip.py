import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'machine',
    'password': 'learning',
    'host': '127.0.0.1',
    'database': 'ObjectDB',
    'raise_on_warnings': True,
}

add_image = ("INSERT INTO image "
             "(path,exif) "
             "VALUES (%s, %s)")

data_image = ('/srv/ObjectDB/test.png', 'NULL') #Testing adding an entry to the image database

try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


cursor = db.cursor() # Create a cursor for MySQL commands
cursor.execute(add_image, data_image)
db.commit()
cursor.close()
db.close()
