class Player:
    def __init__(self):
        print(__name__)
        self.username = ""
        self.email = ""

    def create_user(self, username, email):
        with open("user.txt") as user_file:
            line_read = user_file.readlines()

            does_exists = False
            for line in line_read:
                if line == username + " " + email + "\n":
                    does_exists = True

            if does_exists:
                print("User already exists!")
            else:
                with open("user.txt", "a") as user_file_b:
                    user_file_b.write(username + " " + email + "\n")

    def login_user(self):
        with open("user.txt") as user_file:
            return user_file.readlines()
