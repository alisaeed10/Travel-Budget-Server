from pymongo import MongoClient

client = MongoClient()
# Provide the connection details
hostname = 'mongodb://localhost'
port = 27017

# Create a MongoClient instance
client = MongoClient(hostname, port)

db = client["travel-budget"]
print(collection.name)


# def findUser(email):
#     user = collection.findOne
#     ({
#         "email": email
#     })
#     return user

print("Database connected successfully!!!")