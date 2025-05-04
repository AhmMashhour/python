users=[{"name":"ahmed","pass":"ahm123"},{"name":"mashhour","pass":"mas123"}]

def checkUsers():
    for i in range(len(users)):
        if UserName== users[i]["name"]:
            if password==users[i]["pass"]:
                return True
            else:
                return False
       

UserName=input("Enter your name: ")
password=input("Enter your password: ")       
if checkUsers():
    print(f"Hello {UserName}")
else:
    print("Not valid username or password")
