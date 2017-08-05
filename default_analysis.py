# Read EXIF and ODAPI output from images table.
# Identify different objects by some relevant common factor.
# Consolidate information about individual objects into JSON files in objects table.

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

# Create a cursor for MySQL commands
cursor = db.cursor()

# Iterate through odapi_output
#   Analysis 1
#   Analysis 2
#   ...
