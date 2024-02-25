from database import database

db = database.db # get the database
user_collection = db["users"]

# Insert a document into the collection
def insert_user(email, name, password):
    user_collection.insert_one({"email": email, "name": name, "password": password})
    return "User inserted in db successfully!!!"
    
# get a user from the collection
def get_user(email):
    print("User retrieved successfully!!!")
    user = user_collection.find_one({"email": email})
    if user is not None:
        return {"email": user["email"], "name": user["name"],"password": user["password"]}
    else: 
        return None