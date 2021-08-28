def login(database, username, password):

    username, password = username.strip(), password.strip()

    if username in database: 
        if database.get(username) == password:
            print(f"Welcome {username}")
            return username
        else:
            print("Incorrect password, please try again")
            return ""
    else:
        print("Username and/or password doesn't exist")
        return ""
    
def register(database, username):
    
    if username in database:
        print("Username already exists")
        return ""
    else:
        print("Username created")
        return username