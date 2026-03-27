#Importing from User
from models import User

# Our user dictionary
user_db = {
    "admin": User(1, "admin", "1234", "admin"),
    "user": User(2, "john", "pass", "user")
}

current_user = None

# Loop for login on dashboard
while True:
    if current_user is None:
        print("\n--- LOGIN ---")
        username = input("Username: ")
        password = input("Password: ")

        if username in user_db and user_db[username].password == password:
            current_user = user_db[username]
            print(f"Welcome {current_user.username}!")
        else:
            print("Invalid login details")

    else:
        print("\n--- DASHBOARD ---")
        print("1. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            current_user = None
            print("Logged out successfully")