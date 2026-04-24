import pyodbc

def connect_db():

    conn = pyodbc.connect(

        'DRIVER={SQL Server};'

        'SERVER=YOUR LOCAL SERVER ADDRESS;'

        'DATABASE=ApexLogisticsDB;'

        'Trusted_Connection=yes;'

    )

    return conn

def login(conn):

    cursor = conn.cursor()
    username = input("Enter username: ")

    password = input("Enter password: ")
    # Use parameterized query (prevents SQL injection)

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

def create_product(conn):

    cursor = conn.cursor()
    name = input("Enter product name: ")

    price = input("Enter price: ")

    stock = input("Enter stock quantity: ")
    query = """

    INSERT INTO tblProducts (name, price, stock_qty)

    VALUES (?, ?, ?)

    """
    cursor.execute(query, (name, price, stock))
    conn.commit()
    print("Product added successfully")

def view_products(conn):

    cursor = conn.cursor() 
    query = "SELECT * FROM tblProducts"

    cursor.execute(query)
    products = cursor.fetchall()
    print("\n--- Product List ---")

    for product in products:

        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}")

def menu(conn):

    while True:

        print("\n1. Add Product")

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

            print("Invalid choice")

def main():

    conn = connect_db()
    if login(conn):

        menu(conn)

    else:

        print("Access denied")
if __name__ == "__main__":

    main()