# Read EXIF and ODAPI output from images table.
# Identify different objects by some relevant common factor.
# Consolidate information about individual objects into JSON files in objects table.

from __future__ import print_function
import os
import mysql.connector
from mysql.connector import errorcode
import jsonpickle

# ObjectDB Configuration
config = {
    'user': 'machine',
    'password': 'learning',
    'host': '127.0.0.1',
    'database': 'ObjectDB',
    'raise_on_warnings': True,
}

# Connect to ObjectDB
try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# Change directory to database folder (/srv/ObjectDB)
os.chdir('/srv/ObjectDB')

# Create a cursor for MySQL commands
cursor = db.cursor()

# Iterate through odapi_output
#   Analysis 1
#   Analysis 2
#   ...
odapi_output_filenames=[] # To be populated through database magic.
# Extract all data into an array (does not scale well, but we're pressed for time).
odapi_data_array=[]
os.chdir('/srv/ObjectDB/odapi_output')
for filename in odapi_output_filenames:
    odapi_file=open(filename,'rb')
    odapi_data=jsonpickle.decode(odapi_file.read())
    odapi_file.close()
    odapi_data_array.append(odapi_data)
# Loop through odapi_data_array and populate object_array
object_array=[]
# For reference, odapi_adapter.get_objects(filepath) returns: [
#   num_detections,
#   boxes,
#   scores,
#   classes,
#   image_np,
#   categories,
#   category_index
# ]
for odapi_data in odapi_data_array:
    # image_np: uint8 numpy array with shape (img_height, img_width, 3)
    # boxes: a numpy array of shape [N, 4]
    # classes: a numpy array of shape [N]
    # scores: a numpy array of shape [N] or None.
    # category_index: a dict containing category dictionaries (each holding
    #   category index `id` and category name `name`) keyed by category indices.
    for i in range(odapi_data[1].shape[0]):
        score=odapi_data[3][i]
        if score>.5:
            name_text = 'name: {}'.format(odapi_data[4][odapi_data[2][i]]['name'])
            score_text='score: {}%'.format(int(100*score))
            object_array.append((name_text,score_text))

# Print output
print(object_array)
