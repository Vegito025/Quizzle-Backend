import random
import string
from controllers import app
from flask import jsonify, request, json
from database import Questions, Users
import jwt


@app.route("/getsubmission", methods=["POST"])
def get_submission():
    data = request.get_json()
    access_token = data["access_token"]
    marks = data["marks"]
    ppin = data["ppin"]
    qpin = data["qpin"]

    decoded = jwt.decode(access_token, "LondonBridgeIsFallingDown", algorithms="HS256")
    user_details = Users.find_one({"email": decoded["email"][1:len(decoded["email"]) - 1]})
    question_details = Questions.find_one({"host_pin": int(ppin), "exam_pin": int(qpin)})
    if question_details:
        Questions.update_one({"host_pin": int(ppin), "exam_pin": int(qpin)}, {"$push": {"attempts": {"name": user_details["name"],
                                                                                                     "board": user_details["board"],
                                                                                                     "college": user_details["college"],
                                                                                                     "designation": user_details["designation"],
                                                                                                     "grade": user_details["grade"],
                                                                                                     "roll_no": user_details["rollno"],
                                                                                                     "marks": marks}}})
        return jsonify({"success": True})
