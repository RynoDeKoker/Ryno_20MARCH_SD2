from db_connection import connect_db

def test_connection():
    conn = connect_db()
    if conn : 
        print("Connected successfully!")
        # cursor = conn.cursor()

        # cursor.execute("SELECT * FROM tblProducts")
        # rows = cursor.fetchall()

        # for row in rows:
        #     print(row)

        conn.close()
    else:
        print("Connection failed.")

# if name == "main":
test_connection();