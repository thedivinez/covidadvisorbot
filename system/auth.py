from functools import wraps
from system.config import table, db_query
from flask import redirect, url_for, flash, session, request
from werkzeug.security import generate_password_hash, check_password_hash


class User:
  @staticmethod
  def signin_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
      if 'is_authenticated' in session:
        return func(*args, **kwargs)
      else:
        return redirect(url_for("signin"))

    return wrap

  @staticmethod
  def start_session(user):
    del user['password']
    session['user'] = user
    session['is_authenticated'] = True
    return True

  def signin(self):
    user = table.table("users").get(db_query.email == request.form.get('email'))
    if not user:
      flash('Please sign up before!')
      return redirect(url_for('signup'))
    elif not check_password_hash(user["password"], request.form.get('password')):
      flash('Please check your signin details and try again.')
      return redirect(url_for('signin'))  # if the user doesn't exist or password is wrong, reload the page
    User.start_session(user)
    return redirect(url_for('dashboard'))

  def signup(self):
    user = table.table("users").get(db_query.email == request.form.get('email'))
    if user:  # if a user is found, we want to redirect back to signup page so user can try again
      flash('Email address already exists')
      return redirect(url_for('signup'))
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = dict(request.form)
    new_user["password"] = generate_password_hash(new_user["password"], method='sha256')
    # add the new user to the database
    table.table("users").insert(new_user)
    return redirect(url_for('signin'))