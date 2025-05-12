def login(user: str, password: str):
    if user == "admin" and password == "1234":
        print("Access granted")
    else:
        print("Access denied")

user_id = input('Insert your user id: ')
password = input('Insert your password: ')

login(user_id, password)
