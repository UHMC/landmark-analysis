# Read ODAPI output from images table and folder.
# Identify different objects by kind (name).
# Consolidate information about individual objects into pickled dictionaries (link in objects table of database).

from __future__ import print_function

import os
import pickle
import time
import uuid

import mysql.connector
from mysql.connector import errorcode

SUFFICIENT_SCORE_THRESHOLD = 0.5

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
    # Set autocommit to true, otherwise database connection will be stale
    db.autocommit = True
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# Create a cursor for MySQL commands
cursor = db.cursor()

odapi_output_filenames = []  # To be populated through database magic.

# Database magic
cursor.execute('SELECT odapi_output FROM images')
for row in cursor:
    odapi_output_filenames.append(str(row[0]))

os.chdir('/srv/ObjectDB/odapi_output')
object_dict = {}

# Variable setup
last_entry = 0
known_entry = 0

# Find number of the last entry in the database
cursor.execute("SELECT id FROM images ORDER BY id DESC LIMIT 1")
result=cursor.fetchone()
if result is not None: last_entry=int(result[0])

while (True):
    # Run the for loops if the known entry does not match the last entry  (database updated)
    if (last_entry != known_entry):
        # Become aware of the last entry in the database
        known_entry = last_entry
        for filename in odapi_output_filenames:
            odapi_file = open(filename, 'rb')
            odapi_data = pickle.load(odapi_file)
            odapi_file.close()
            # Populate object_dict.
            # odapi_data is a tuple containing:
            #   image_np: uint8 numpy array with shape (img_height, img_width, 3)
            #   boxes: a numpy array of shape [N, 4]
            #   classes: a numpy array of shape [N]
            #   scores: a numpy array of shape [N] or None.
            #   category_index: a dict containing category dictionaries (each holding
            #       category index `id` and category name `name`) keyed by category indices.
            for i in range(odapi_data[1].shape[0]):
                score = odapi_data[3][i]
                if score >= SUFFICIENT_SCORE_THRESHOLD:
                    name = odapi_data[4][odapi_data[2][i]]['name']
                    if name in object_dict:
                        object_dict[name][1].append(score)
                        object_dict[name][2].append(filename)
                    else:
                        object_dict[name] = [name, [score], [filename]]

        # Actual analysis
        os.chdir('/srv/ObjectDB/analysis')
        for name in object_dict:
            obj = object_dict[name]
            # For each object:
            #   - number of images this kind appears in across database
            num_images = len(set(obj[2]))
            #   - total number of times it appears in the database
            num_appearances = len(obj[1])
            #   - simple mean of percent match scores across database
            mean_score = sum(obj[1]) / float(len(obj[1]))
            # Put these in the database and file system ^
            analysis_output = {
                name: obj,
                "num_images": num_images,
                "num_appearances": num_appearances,
                "mean_score": mean_score
            }
            analysis_file = open(uuid.uuid4().hex + '-analysis.pickle', 'wb')
            pickle.dump(analysis_output, analysis_file)
            cursor.execute("INSERT INTO objects (analysis) VALUE (\""+analysis_file.name+"\");")
            analysis_file.close()
            # Print output
            print(analysis_output)
    # Refresh the last entry from database
    cursor.execute("SELECT id FROM images ORDER BY id DESC LIMIT 1")
    result=cursor.fetchone()
    if result is not None: last_entry=int(result[0])
    time.sleep(3)
