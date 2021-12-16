from app.controllers.controller import ControllerBase
from flask import render_template

class CalController(ControllerBase):
    @staticmethod
    def get():
        return render_template('cal.html')
