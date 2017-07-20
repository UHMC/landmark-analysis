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

# Connecting to the Database using config
try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# Changing working directory to unprocessed folder
os.chdir('/srv/ObjectDB/unprocessed')
cursor = db.cursor() # Create a cursor for MySQL commands

# Loop forever
while(True):
	files = os.listdir('.') # Populate list of files
	if(files != ''): # Only run when folder is not empty
		for x in files:
			print('Processing file: '+x) 
			f = open(x,'rb') # Open the file 
			os.system('mv '+x+' ../processed/') # Move file to processed folder
			exif=jsonpickle.encode(exifread.process_file(f)) # Extract EXIF into JSON
			with open(x+".json", 'wb') as output:
				os.chdir('/srv/ObjectDB/EXIF')
				output.write(exif)
				os.chdir('/srv/ObjectDB/unprocessed')
			data_image = ('/srv/ObjectDB/sorted/'+x,'/srv/ObjectDB/EXIF/'+x+'.json') # Information to be added to the database
			cursor.execute( add_image, data_image) # Add item to the database
			db.commit() # Commit changes to database
	time.sleep(1)
	print('Waiting for files...')
