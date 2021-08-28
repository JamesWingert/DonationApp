from donations_pkg.homepage import show_homepage, donate
from donations_pkg.user import login, register

import sys


database = {"admin":"password123"}
donations = []
authorized_user = ""

show_homepage()

if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as:{authorized_user}")


while True:
    show_homepage()
    user_choice = input("Please select an option by typing the number corresponding with your choice:\n")

    if user_choice == "1":
        username = input("Username:\n")
        password = input("Password:\n")
        
        authorized_user = login(database, username, password)
        
    elif user_choice == "2":
        print("Please enter your username and password you'd like to register:")
        username = input("Username:\n")
        password = input("Password:\n")
        
        authorized_user = register(database, username)
        
        if authorized_user != "":
            database[username] = password
        
    elif user_choice == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
        
    elif user_choice == "4":
        #Print: TODO: Write Show Donations Functionality".
        show_homepage()
        
    elif user_choice == "5":
        sys.exit("Goodbye")