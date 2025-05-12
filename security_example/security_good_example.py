import hashlib

USER_DB = {
    "admin": hashlib.sha256("secure_password".encode()).hexdigest()
}

def hash_password(password:str):
    return hashlib.sha256(password.encode()).hexdigest()

def login(user, password):
    if user in USER_DB and USER_DB[user] == hash_password(password):
        return "Access granted"
    
    return "Access denied"