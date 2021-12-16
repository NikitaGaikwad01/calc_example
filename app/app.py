"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.oop_controller import OopController
from app.controllers.cal_controller import CalController
from app.controllers.pylint_controller import PylintController
from app.controllers.aaa_controller import AaaController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/oop", methods=['GET'])
def oop_get():
    return OopController.get()
@app.route("/oop", methods=['POST'])
def oop_post():
    return OopController.post()

@app.route("/cal", methods=['GET'])
def cal_get():
    return CalController.get()
@app.route("/cal", methods=['POST'])
def cal_post():
    return CalController.post()

@app.route("/pylint", methods=['GET'])
def pylint_get():
    return PylintController.get()
@app.route("/pylint", methods=['POST'])
def pylint_post():
    return PylintController.post()

@app.route("/aaa", methods=['GET'])
def aaa_get():
    return AaaController.get()
@app.route("/aaa", methods=['POST'])
def aaa_post():
    return AaaController.post()

