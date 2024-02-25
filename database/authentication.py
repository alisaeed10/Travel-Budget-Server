from database import database

db = database.db # get the database
user_collection = db["users"]

# Insert a document into the collection
def insert_user(email, name, password,confrim_password):
    user_collection.insert_one({"email": email, "name": name, "password": password,"confirm_password": confrim_password})
    print("User inserted successfully!!!")
    
# get a user from the collection
def get_user(email, password):
    print("User retrieved successfully!!!")
    user = user_collection.find_one({"email": email})
    print(user)
    return {"email": user["email"], "name": user["name"]}