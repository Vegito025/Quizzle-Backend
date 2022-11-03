from flask import Flask

app = Flask(__name__)

from controllers.auth import welcome, register, login, getdetail, getinfo, setTutor
from controllers.Questions import getQuestions, getpins, getexam, getSubmission, getresults