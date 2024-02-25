from pymongo import MongoClient

client = MongoClient()
# Provide the connection details
hostname = 'mongodb://localhost'
port = 27017

# Create a MongoClient instance
client = MongoClient(hostname, port)

db = client["travel-budget"]

print("Database connected successfully!!!")