import mysql.connector as mysql
import sys

from dvc.prompt import password


class dbhelper:
    def __init__(self):
        try:
            self.conn = mysql.connect(
                host='localhost',
                user='root',
                password='',
                database='db_demo_crud_app'
            )
            self.cursor = self.conn.cursor()
            print("Database connection established successfully!")
        except mysql.Error as err:
            print(f"Database connection failed: {err}")
            sys.exit(1)

    # Stop program if DB connection fails
    def register(self,name,email,password):

        query = "INSERT INTO login (name, email, pass) VALUES (%s, %s, %s)"
        values = (name, email, password)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("User registered successfully!")
if __name__ == "__main__":
    db = dbhelper()
