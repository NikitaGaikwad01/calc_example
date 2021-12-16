from app.controllers.controller import ControllerBase
from flask import render_template

class OopController(ControllerBase):
    @staticmethod
    def get():
        return render_template('oop.html')
