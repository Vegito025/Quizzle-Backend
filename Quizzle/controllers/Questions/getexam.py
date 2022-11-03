from flask import request, jsonify
import jwt
from controllers import app
from database import Questions


@app.route("/getexam", methods=["POST"])
def get_exam():
    data = request.get_json()
    hostpin = data["hostpin"]
    exampin = data["exampin"]
    result = Questions.find_one({"host_pin": int(hostpin), "exam_pin": int(exampin)})
    return jsonify({"success": True, "data": result["questions"]})
