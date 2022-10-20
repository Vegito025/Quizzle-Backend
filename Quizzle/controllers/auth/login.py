from werkzeug.security import check_password_hash
from controllers import app
from flask import jsonify, request, json
from database import Users
import jwt


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    register_type = data["type"]
    if register_type == "google":
        data["password"] = None
    password = data["password"]
    result = Users.find_one({"email": email})
    if not result:
        return jsonify({'success': False, "message": "This user does not exist"})
    elif result and register_type == "google":
        access_token = jwt.encode({"email": json.dumps(result["email"], default=str)}, "LondonBridgeIsFallingDown",
                                  algorithm="HS256")
        return jsonify({"success": True, "access_token": access_token})

    else:
        access_token = jwt.encode({"email": json.dumps(result["email"], default=str)}, "LondonBridgeIsFallingDown",
                                  algorithm="HS256")
        if check_password_hash(result["password"], password):
            return jsonify({"success": True, "access_token": access_token})
        else:
            return jsonify({"success": True, "message": "Password does not match with the current user."})
