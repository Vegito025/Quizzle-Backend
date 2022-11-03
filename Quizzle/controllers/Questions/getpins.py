import random
import string
from controllers import app
from flask import jsonify, request, json
from database import Questions, Users
import jwt

@app.route("/getpin", methods=["POST"])
def get_pin():
    data = request.get_json()
    ppin = data["ppin"]
    qpin = data["qpin"]
    results = Questions.find_one({"host_pin": int(ppin), "exam_pin": int(qpin)})
    if results:
        return jsonify({"success": True})
    else:
        return jsonify({"success":False})