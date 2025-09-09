from db_helper import dbhelper as db

class Flipkart:
    def __init__(self):
        # Connect to DB
        self.db = db()
        self.menu()

    def menu(self):
        while True:  # Keep showing menu until user exits
            user_input = input("""
            1. Register
            2. Login
            3. Exit
            Enter your choice: """).strip()

            if user_input == '1':
                self.register()
            elif user_input == '2':
                self.login()
            elif user_input == '3':
                print("Exited successfully.")
                break
            else:
                print("Invalid input. Please try again.")

    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        respones=self.db.register(name, email, password)
        if respones:
            print("User registered successfully.")
            self.menu()
        else:
            print("User registration failed.")

    def login(self):
        # Example placeholder
        print("Login functionality goes here.")
        # e.g. self.db.validate_user(email, password)


if __name__ == "__main__":
    Flipkart()
