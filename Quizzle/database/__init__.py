import pymongo
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = pymongo.MongoClient(os.getenv("MONGO_DB"), serverSelectionTImeoutMS=5000)

try:
    if client.server_info():
        print("Successfully connected to the database")
except Exception:
    print("Unable to connect to the server")

from database.Users import Users
from database.Questions import Questions
