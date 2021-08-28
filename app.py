from donations_pkg.homepage import show_homepage
import sys

database = {"admin":"password123"}
donations = []
authorized_user = []

show_homepage()

if authorized_user == []:
    print("You must be logged in to donate.")
else:
    print(f"Logged in as:{authorized_user}")

user_choice = input("Please select an option by typing the number corresponding with your choice")
if user_choice == 1:
    print("Please enter your username and password:")
    Print "TODO: Write Login Functionality".
    show_homepage()
if user_choice == 2:
    print("Please enter your username and password you'd like to register:")
    Print "TODO: Write Register Functionality".
    show_homepage()
if user_choice == 3:
    Print "TODO: Write Donate Functionality".
    show_homepage()
if user_choice == 4:
    Print: TODO: Write Show Donations Functionality".
    show_homepage()
if user_choice == 5:
    sys.exit("Goodbye")