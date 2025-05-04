users = [
    {"name": "omar", "pass": "123"},
    {"name": "ahmed", "pass": "456"}
]

def find_user(username, users):
    for user in users:
        if user["name"] == username:
            return user
    return None

def check_password(user):
    attempts = 3
    while attempts > 0:
        password = input("Enter your password: ")
        if password == user["pass"]:
            print("Welcome!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong password. You have {attempts} attempt(s) left.")
            else:
                print("Account locked. Too many failed attempts.")
    return False

def main():
    username = input("Enter your name: ")
    user = find_user(username, users)
    
    if user:
        check_password(user)
    else:
        print("Invalid username.")

main()
