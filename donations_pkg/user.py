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