# File to signup new user

# Import the required module
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ALICE")

# Create a cursor object
my_cursor = mydb.cursor()


def sign_up():
    # Take user input for name, username, and password
    name = input("Enter your name: ")
    username = input("Enter your desired username: ")
    password = input("Enter your password: ")

    # Execute the SQL query to insert new user data into the database
    my_cursor.execute("INSERT INTO login_info(name, UserID, Password) VALUES (%s, %s, %s)", (name, username, password))

    # Commit the transaction
    mydb.commit()
    print("Data inserted successfully")
