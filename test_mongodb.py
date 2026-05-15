
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ankitv8005_db_user:ankit7268@cluster0.q7eutkk.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)