import bcrypt
import re

# to hash a password you need to use bcrypt and use the bulit in functions:
    # bcrypt.gensalt()
        # generates a salt for you to use when hashing your password
    # bcrypt.hashpw(password, bcrypt.gensalt()) 
        # which which will return a hashed password that combines your password and a random salt genrated by bcrypt
    # bcrypt.checkpw(password, hashed)
        # checks if the hash password is the same as the password you provided
    
# encrypting password:
def encrypt(password):
    password = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=14)
    hashed_password = bcrypt.hashpw(password,salt)
    print("Hashed Password: ", hashed_password)
    return hashed_password
    
# if password is valid:
def validation(password,confirm_password):
    symbols = r'[a-zA-Z#$%0-9]'
    if (password == confirm_password) and (len(password) >= 8 and len(confirm_password) >= 8) and (re.match(symbols, password) and re.match(symbols, confirm_password)):
        return True
    
    return False

# decrypting password:
def decrypt(password,hashed_password):
    password = password.encode('utf-8')
    if bcrypt.checkpw(password,hashed_password):
        return True
    
    return False


