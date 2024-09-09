from config import get_user_by_username

def login(username, password):
    user = get_user_by_username(username)
    
    if user is not None:
        stored_password = user['password']
        if password == stored_password:
            return True
    return False
