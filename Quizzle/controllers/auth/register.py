from werkzeug.security import generate_password_hash
from controllers import app
from flask import jsonify, request, json
from database import Users
from bson.objectid import ObjectId
import jwt
import string
import random


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    register_type = data["type"]
    if register_type == "google":
        data["password"] = None
        data["confirmed_password"] = None
    password = data["password"]
    confirm_password = data["confirmed_password"]
    profile_pic = data["profile_pic"]
    profile_status = data["profile_status"]

    result = Users.find_one({"email": email})
    if result and register_type == "google":
        access_token = jwt.encode({"email": json.dumps(result["email"], default=str)}, "LondonBridgeIsFallingDown",
                                  algorithm="HS256")
        return jsonify({"success": True, "access_token": access_token})
    if result:
        return jsonify({'success': False, "message": "User Already Exists"})

    else:
        if register_type == "google":
            S = 24
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
            Users.insert_one({
                "name": name,
                "email": email,
                "type": "google",
                "password": str(ran),
                "profile_pic": profile_pic,
                "profile_status": profile_status,
                "tutorial" : False,
                "personal_pin": None
            })
            result = Users.find_one({"email": email})
            access_token = jwt.encode({"email": json.dumps(result["email"], default=str)}, "LondonBridgeIsFallingDown",
                                      algorithm="HS256")
            return jsonify({"success": True, "access_token": access_token})
        elif password == confirm_password:
            hashed_password = generate_password_hash(
                password,
                method="pbkdf2:sha256",
                salt_length=8
            )
            Users.insert_one({
                "name": name,
                "email": email,
                "password": hashed_password,
                "type": "manual",
                "profile_status": profile_status,
                "profile_pic": None,
                "tutorial": False,
                "personal_pin": None
            })
            result = Users.find_one({"email": email})
            access_token = jwt.encode({"email": json.dumps(result["email"], default=str)}, "LondonBridgeIsFallingDown",
                                      algorithm="HS256")
            return jsonify(
                {"success": True, "message": "Welcome User To The World Of Quizzle", "access_token": access_token})
