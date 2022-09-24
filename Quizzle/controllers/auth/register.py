from werkzeug.security import generate_password_hash
from controllers import app
from flask import jsonify, request, json
from database import Users
from random import randint
from bson.objectid import ObjectId
import jwt


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    password = data["password"]
    confirm_password = data["confirmed_password"]
    institution = data["institution"]
    result = Users.find_one({"email": email})
    if result:
        return jsonify({'success': False, "message": "User Already Exists"})
    else:
        if password == confirm_password:
            hashed_password = generate_password_hash(
                password,
                method="pbkdf2:sha256",
                salt_length=8
            )
            Users.insert_one({
                "name": name,
                "email": email,
                "password": hashed_password,
                "institution": institution
            })
            result = Users.find_one({"email": email})
            access_token = jwt.encode({"_id": json.dumps(result["_id"], default=str)}, "GetSomeBitches",
                                      algorithm="HS256")
            return jsonify(
                {"success": True, "message": "Welcome User To The World Of Quizzle", "access_token": access_token})
