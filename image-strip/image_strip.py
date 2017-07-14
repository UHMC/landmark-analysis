import mysql.connector
from mysql.connector import errorcode
import exifread
import os
import time
import jsonpickle


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


data_image = ('NULL','NULL')
try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


os.chdir('/srv/ObjectDB/unprocessed')
cursor = db.cursor() # Create a cursor for MySQL commands
while(True):
	files = os.listdir('.')
	if(files != ''):
		for x in files:
			print('Processing file: '+x)
			f = open(x,'rb')
			os.system('mv '+x+' ../processed/')
			exif=jsonpickle.encode(exifread.process_file(f))
			data_image = ('/srv/ObjectDB/sorted/'+x,exif)
			cursor.execute( add_image, data_image)
			db.commit()
	time.sleep(1)
	print('Waiting for files...')

