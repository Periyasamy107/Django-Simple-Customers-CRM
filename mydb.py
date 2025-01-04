
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    passwd = '123456'
)

# Cursor Object 

cursorObject = database.cursor()

# Create a database 

cursorObject.execute('CREATE DATABASE customer_details')

print('Created Database Successfully!!')