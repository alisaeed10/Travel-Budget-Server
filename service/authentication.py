#serivce is used for validation (like if they dont provide a username) and calculation
from database import authentication
from models import User

def test():
    return "hello world"

def create_user(user: User.User):
    print("Service", user.email, user.name, user.password)
    authentication.insert_user(user.email, user.name, user.password, user.confirm_password)
    print("User created successfully in Service!!!")
    
def get_user(email: str, password: str):
    print("Service", email, password)
    user = authentication.get_user(email, password)
    return user
    
    
# testing if the user input is correct