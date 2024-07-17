import mysql.connector
import bcrypt

# Connect to the database
# I used sqlfreedatabase so this setup might be different
cnx = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='',
    port=3306
)

cursor = cnx.cursor()

def register_user():
    # Prompt the user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert the user's information into the database
    insert_query = "INSERT INTO user_info (username, password) VALUES (%s, %s)"
    cursor.execute(insert_query, (username, hashed_password.decode('utf-8')))
    cnx.commit()

    print("Registration successful!")

def login_user():
    while True:
        # Prompt the user for username and password
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Retrieve the hashed password from the database based on the username
        select_query = "SELECT password FROM user_info WHERE username = %s"
        cursor.execute(select_query, (username,))
        result = cursor.fetchone()

        if result is None:
            print("Invalid username or password.")
            continue

        hashed_password = result[0].encode('utf-8')

        # Verify the entered password with the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("Login successful!")
            return username
        else:
            print("Invalid username or password.")

def close_connection():
    cursor.close()
    cnx.close()



