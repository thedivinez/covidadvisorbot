from system.auth import User
from system.config import app
from system.engine import CovidScreaning
from flask import render_template, jsonify, request


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/dashboard")
@User.signin_required
def dashboard():
  return render_template("dashboard.html", subjects=CovidScreaning.getdata())


@app.route("/newmessage")
def newmessage():
  message = {"ip_address": request.args.get("ip_address"), "message": request.args.get("message")}
  response = jsonify(message=CovidScreaning.listen(message))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response


@app.route('/signin', methods=['GET', 'POST'])
def signin():
  # if the request is a GET we return the signin page else try to sign the user in
  return render_template('signin.html') if request.method == 'GET' else User().signin()


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  # If the request is GET we return the sign up page and forms
  # if the request is POST, then we check if the email doesn't already exist and then we save data
  return render_template('signup.html') if request.method == 'GET' else User().signup()


if __name__ == "__main__":
  app.run(debug=True)