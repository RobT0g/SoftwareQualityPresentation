import hashlib

USER_DB = {
    "admin": hashlib.sha256("1234".encode()).hexdigest()
}

def hash_password(password:str):
    return hashlib.sha256(password.encode()).hexdigest()

def login(user, password):
    if user in USER_DB and USER_DB[user] == hash_password(password):
        print("Access granted")
    
    else:
        print("Access denied")

user_id = input('Insert your user id: ')
password = input('Insert your password: ')

login(user_id, password)