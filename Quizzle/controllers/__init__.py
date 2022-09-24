from flask import Flask

app = Flask(__name__)

from controllers.auth import welcome, register