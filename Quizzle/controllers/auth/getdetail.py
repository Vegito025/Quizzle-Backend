from bson import json_util
from werkzeug.security import check_password_hash
from controllers import app
from flask import jsonify, request, json
from database import Users
from random import randint
from bson.objectid import ObjectId

import jwt


@app.route("/getdetail", methods=["POST"])
def get_detail():
    data = request.get_json()
    access_token = data["access_token"]

    decoded = jwt.decode(access_token, "LondonBridgeIsFallingDown", algorithms="HS256")
    result = Users.find_one({"email": decoded["email"][1:len(decoded["email"])-1]})
    result = json.loads(json_util.dumps(result))
    return jsonify({"data": result})
