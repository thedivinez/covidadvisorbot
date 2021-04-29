import os
from flask import Flask
from tinydb import TinyDB, Query

app = Flask(__name__)
db_query = Query()
app.templates_auto_reload = True
app.secret_key = "s-u-p-e-r-s-e-c-r-e-t-k-e-y"
app.static_folder = os.path.join(os.getcwd(), "static")
app.template_folder = os.path.join(os.getcwd(), "templates")
table = TinyDB(os.path.join(os.getcwd(), "static", "db", "covidscreening.db"))