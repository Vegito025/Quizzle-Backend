import os
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS
import pymongo
from controllers import app

load_dotenv(find_dotenv())
CORS(app)

client = pymongo.MongoClient(os.getenv("MONGO_DB"), serverSelectionTimeoutMS=5000)

if __name__ == "__main__":
    app.run(debug=True)
