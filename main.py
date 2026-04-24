# Simple User Authentication System
# Importing from User
from models import User

# Our user dictionary
user_db = {
    "admin": User(1, "admin", "1234", "Admin"),
    "john": User(2, "john", "pass", "Customer"),
    "sarah": User(3, "sarah", "abc", "Customer")
}

# Variable to track the currently logged-in user
current_user = None
# Loop for login on dashboard
while True:
    
    # If no user is currently logged in, prompt for login credentials
    if current_user is None:
        print("\n=== LOGIN ===")
        username = input("Enter username: ")
        password = input("Enter password: ")

# Check if the entered username exists in the user database
        if username in user_db:
            user = user_db[username]
            
            if user.password == password:
                current_user = user
                print(f"Welcome, {user.username}!")
            else:
                print("Incorrect password.")
        else:
            print("User not found.")

# If a user is logged in, display the dashboard with options to logout or exit
    else:
        print("\n=== DASHBOARD ===")
        print(f"Logged in as: {current_user.username} ({current_user.role})")
        print("1. Logout")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print("Logging out...")
            current_user = None

        elif choice == "2":
            print("Exiting system...")
            break

        else:
            print("Invalid option.")
