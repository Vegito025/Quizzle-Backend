import random
import string
from controllers import app
from flask import jsonify, request, json
from database import Questions, Users
import jwt


@app.route("/getquestions", methods=["POST"])
def get_questions():
    data = request.get_json()
    access_token = data["access_token"]
    questions = data["questions"]

    decoded = jwt.decode(access_token, "LondonBridgeIsFallingDown", algorithms="HS256")
    results = Users.find_one({"email": decoded["email"][1:len(decoded["email"]) - 1]})
    S = 6
    ran = random.randint(100000, 999999)
    if not results["personal_pin"]:
        Users.update_one({"email": decoded["email"][1:len(decoded["email"]) - 1]}, {"$set": {"personal_pin": ran}})
    else:
        ran = results["personal_pin"]
    V = 6
    exam_pin = random.randint(100000, 999999)
    Questions.insert_one({"host_pin": ran, "exam_pin":exam_pin, "questions":questions})
    results = Users.find_one({"email": decoded["email"][1:len(decoded["email"]) - 1]})
    return jsonify({"success": True, "exam_pin": exam_pin, "personal_pin": results["personal_pin"]})


