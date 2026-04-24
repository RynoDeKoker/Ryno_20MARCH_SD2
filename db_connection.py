
#Database connection module using pyodbc to connect to a SQL Server database

import pyodbc

def connect_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=localhost\SQLEXPRESS;' #localhost\SQLEXPRESS
            'DATABASE=ApexLogistics;'
            'Trusted_Connection=yes;'
        )
        return conn
    except Exception as e:
        print("Connection failed:", e)
        return None