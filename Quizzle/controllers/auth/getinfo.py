import os

from werkzeug.security import check_password_hash
from controllers import app
from flask import jsonify, request, json
from database import Users
import jwt
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@app.route("/getinfo", methods=["POST"])
def get_info():
    data = request.get_json()
    college = data["college"]
    grade = data["grade"]
    board = data["board"]
    rollno = data["rollno"]
    access_token = data["access_token"]
    status = data["status"]

    decoded = jwt.decode(access_token, os.getenv("JWT_SECRET"), algorithms="HS256")
    Users.update_one({"email": decoded["email"][1:len(decoded["email"]) - 1]}, {"$set": {
        "college": college,
        "grade": grade,
        "board": board,
        "rollno": rollno,
        "profile_status": status
    }})

    return jsonify({"success": True})