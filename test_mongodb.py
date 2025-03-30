
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://rohitkmahaur:Rohit123@cluster1.igjeagq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    db = client.test
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)