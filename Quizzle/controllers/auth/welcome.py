from controllers import app
from flask import jsonify


@app.route("/")
def home():
    return jsonify({"success": True, "message": "Welcome To Quizzle"})
