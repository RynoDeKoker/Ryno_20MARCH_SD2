from models import User

user_db = {
    "admin": User(1, "admin", "1234", "Admin"),
    "john": User(2, "john", "pass", "Customer"),
    "sarah": User(3, "sarah", "abc", "Customer")
}

current_user = None

while True:
    
    if current_user is None:
        print("\n=== LOGIN ===")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in user_db:
            user = user_db[username]
            
            if user.password == password:
                current_user = user
                print(f"Welcome, {user.username}!")
            else:
                print("Incorrect password.")
        else:
            print("User not found.")

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