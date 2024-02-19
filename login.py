# File to check user details and login

# Import necessary module
import mysql.connector

# Establish connection with MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ALICE"
)


# Function to check login credentials
def login():
    my_cursor = mydb.cursor()

    username = input("Enter username: ")
    password = input("Enter your password: ")

    # Execute SQL query to check username and password
    my_cursor.execute("SELECT * FROM login_info WHERE UserID = %s AND Password = %s", (username, password))

    # Fetch result of the query
    my_result = my_cursor.fetchall()

    # Check if user exists in the database
    if my_result:
        return True
    else:
        return False
