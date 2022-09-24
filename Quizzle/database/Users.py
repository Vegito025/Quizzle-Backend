from database import client
import pymongo

Users = client["Users"]["Auth"]
Users.create_index([("email", pymongo.ASCENDING)], unique=True)