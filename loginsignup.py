import sqlite3

firstName = ""
lastName = ""
username = ""
password = ""

def intro():
    return input("Login or Signup: ")

userAccount = {}

    
hasUpper = False
hasNumber = True
enoughDigits = False
letterCounter = 0

def signup():

    global firstName
    global lastName
    global username
    global password

    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    username = input("Username: ")
    password = input("Password (at least 1 CAPITAL LETTER and at least 8 LETTERS): ")
    
    for letter in password:
        global letterCounter
        letterCounter += 1
        if letter.isupper():
            global hasUpper
            hasUpper = True
    
    """if password.isalpha():
        global hasNumber
        hasNumber == False
        print(hasNumber)


    if hasUpper == False or hasNumber == False:
        print("Password does not match rules, try again")
        signup()"""

    if hasUpper == False or letterCounter < 8:
        print("Password does not match rules, try again")
        signup() 

    #global userAccount
    
    #userAccount = {
        #"First Name": firstName, 
        #"Last Name": lastName, 
        #"Username": username,
        #"Password": password
    #}

    print("Signed up!")


connection = sqlite3.connect("UserAccountDatabase.db") #set up connection

cursor = connection.cursor() #set up cursor

def connectDatabase():

    createTable = """CREATE TABLE IF NOT EXISTS users 
    (firstName TEXT, 
    lastName TEXT, 
    username TEXT, 
    password TEXT)
    """
    #create database table

    cursor.execute(createTable) #execute table creation
    
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ? )", (firstName, lastName, username, password)) #populate database 

    cursor.execute("SELECT * FROM users") #select query to get information from table
    
    connection.commit() #commit to databse SO IMPORTANT DONT FORGET THIS

    #cursor.close() # to close database

def deleteUser(deletedUsername):

    cursor.execute("DELETE FROM users WHERE username = ?", (deletedUsername,)) 
    #add a comma after parameter if you get BINDINGS error

    connection.commit()

    print("User deleted")

attempts = 1

def login():
    username = input("Username: ")
    password = input("Password: ")

    global cursor

    cursor.execute("SELECT * FROM users") #need select first to get all users

    allUsers = cursor.fetchall()

    userFound = False

    for user in allUsers:
        if username == user[2] and password == user[3]:
            print("User found, Welcome " + user[0])
            userFound = True
            
            #DELETION PROGRAM: EXAMPLE OF STUFF U COULD DO IF LOGIN SUCCESSFUL
            #deletion = input("Would you like to delete a user? ")
            
            #if deletion == "yes" or deletion == "Yes":
                #deletedUser = input("What username would you like to delete: ")
                #deleteUser(deletedUser)

            #else:
                #print("Program ended")

    global attempts

    if userFound == False:

        if attempts < 4:
            print("Incorrect username/password, please try again ")
            attempts += 1
            login()
            
        if attempts == 4:
            print("You are on your last attempt before being locked out")
            attempts += 1
            login()
    
        if attempts == 5:
            print("You have been locked out due to too many failed attempts")
            exit()
        

            
got_response = False

while got_response == False:

    name = intro()
    if name == "Signup" or name == "signup":
        print("Sign up page: ")
        got_response = True
        signup()
        
    elif name == "Login" or name == 'login':
        print("Login page: ")
        got_response = True
        login()
    else:
        print("Invalid, try again")

connectDatabase()