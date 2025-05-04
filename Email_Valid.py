def get_valid_name():
    name = input("Enter your name: ")
    while name == "" or name.isdigit():
        print("Please enter a valid name.")
        name = input("Enter your name: ")
    return name

def is_valid_email(email):
    return (
        "@" in email and
        "." in email and
        email.index("@") > 0 and
        email.rindex(".") > email.index("@") + 1 and
        not email.startswith(".") and
        not email.endswith(".") and
        ".." not in email and
        " " not in email
    )

def get_valid_email():
    email = input("Enter your email: ")
    while not is_valid_email(email):
        print("Please enter a valid email address.")
        email = input("Enter your email: ")
    return email

def main():
    name = get_valid_name()
    email = get_valid_email()

    print("\n--- User Info ---")
    print("Name:", name)
    print("Email:", email)
    print("Email is valid")

main()
