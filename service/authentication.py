#serivce is used for validation (like if they dont provide a username) and calculation
from database import authentication
from models import User
from utils import passwordFunctions

def test():
    return "hello world"

def create_user(user: User.User):
    print("Service", user.email, user.name, user.password)
    # checking if password is valid
    if passwordFunctions.validation(user.password, user.confirm_password) == False:
        return "Invalid Password"
    
    # ecrypting password and instering into the db
    hash_password = passwordFunctions.encrypt(user.password)
    
    # check if user already in db 
    existing_user = authentication.get_user(user.email)
    if existing_user is not None:
        return "Email already exists"
    
    return authentication.insert_user(user.email, user.name, hash_password)
    
    
def get_user(email: str, password: str):
    print("Service", email, password)

    # getting the user from the db and decrypting the password
    user = authentication.get_user(email)
    if user is not None:
        decrypted_password = passwordFunctions.decrypt(password, user["password"])
        if decrypted_password == True:
            return {"email": user["email"], "name": user["name"]}
    return "User Not Found"