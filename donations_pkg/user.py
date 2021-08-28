def login(database, username, password):
    database = {}
    username = ""
    password = ""
    
    username, password = username.strip(), password.strip()
    
    if database.get(username) == password:
       print(f"Welcome {username}")
       return username
    elif username in database and password not in database:
        print("Incorrect password, please try again")
        return ""
    else:
        print("Incorrect username and password")   
        return "" 