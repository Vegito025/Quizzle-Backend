from controllers import app
from flask import jsonify, request
from database import Users
import jwt


@app.route("/finishtutor", methods=["POST"])
def finish_tutor():
    data = request.get_json()
    access_token = data["access_token"]
    tutorial = data["tutorial"]

    decoded = jwt.decode(access_token, "LondonBridgeIsFallingDown", algorithms="HS256")
    Users.update_one({"email": decoded["email"][1:len(decoded["email"]) - 1]}, {"$set": {"tutorial": True}})

    return jsonify({"success": True})
