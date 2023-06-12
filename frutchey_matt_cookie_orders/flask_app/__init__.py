from flask import Flask
app = Flask(__name__)
app.secret_key = "ChooseAKeyOrLeaveThisAlone"
from flask_app.controllers import orders
