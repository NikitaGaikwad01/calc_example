from app.controllers.controller import ControllerBase
from flask import render_template

class PylintController(ControllerBase):
    @staticmethod
    def get():
        return render_template('pylint.html')
