from database import db

user_collection = db["users"]

# Insert a document into the collection
def insertUser(email, name, password):
    user_collection.insert_one({"email": email, "name": name, "password": password})
    print("User inserted successfully!!!")