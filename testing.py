import pyodbc


# DATABASE CONNECTION
def connect_db():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=YOUR LOCAL SERVER ADDRESS;'
        'DATABASE=ApexLogisticsDB;'
        'Trusted_Connection=yes;'
    )
    return conn


# LOGIN FUNCTION
def login(conn):
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    query = """
    SELECT * FROM tblUsers
    WHERE username = ? AND password = ?
    """

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful")
        return True
    else:
        print("Invalid login")
        return False


# CREATE PRODUCT (INSERT INTO tblProducts)
def create_product(conn):
    cursor = conn.cursor()

    name = input("Enter product name: ")

    try:
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Invalid input. Price must be a number and stock must be an integer.")
        return

    query = """
    INSERT INTO tblProducts (name, price, stock_qty)
    VALUES (?, ?, ?)
    """

    cursor.execute(query, (name, price, stock))
    conn.commit()

    print("Product added successfully")


# VIEW PRODUCTS (READ FROM tblProducts)
def view_products(conn):
    cursor = conn.cursor()

    query = "SELECT * FROM tblProducts"
    cursor.execute(query)

    products = cursor.fetchall()

    print("\n--- Product List ---")

    if not products:
        print("No products found.")
        return

    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}")


# MENU SYSTEM (RUNS UNTIL USER EXITS)
def menu(conn):
    while True:
        print("\n===== MENU =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_product(conn)
        elif choice == "2":
            view_products(conn)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")


# MAIN PROGRAM (LOGIN FIRST, THEN MENU)
def main():
    conn = connect_db()

    if login(conn):
        menu(conn)
    else:
        print("Access denied")


if __name__ == "__main__":
    main()