from flask import render_template
from system.engine import CovidScreaning
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html", subjects=CovidScreaning.getdata())


@app.route("/newmessage")
def newmessage():
  message = {"ip_address": request.args.get("ip_address"), "message": request.args.get("message")}
  response = jsonify(message=CovidScreaning.listen(message))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response


if __name__ == "__main__":
  app.run()