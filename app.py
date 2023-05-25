import os
from flask import Flask, render_template, request
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD

from forms import CoinForm, RegisterForm, LoginForm
import pandas as pd
from pandas import DataFrame
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from models import User


# # Flask Login
# from flask_login import (
#     UserMixin,
#     login_user,
#     LoginManager,
#     current_user,
#     logout_user,
#     login_required,
# )
# login_manager = LoginManager()
# login_manager.session_protection = "strong"
# login_manager.login_view = "login"
# login_manager.login_message_category = "info"
# import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

# @login_manager.user_loader
# def user_loader(user_id):
#     """Given *user_id*, return the associated User object.

#     :param unicode user_id: user_id (email) user to retrieve

#     """
#     return User.query.get(user_id)

# def validate_email(self, email):
#         if User.query.filter_by(email=email.data).first():
#             raise ValidationError("Email already registered!")

# def validate_uname(self, uname):
#     if User.query.filter_by(username=username.data).first():
#         raise ValidationError("Username already taken!")

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# # Register route
# @app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
# def register():
#     form = register_form()

#     return render_template("auth/register.html",form=form)

# # Login route
# @app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
# def login():
#     form = login_form()

#     return render_template("auth/login.html",form=form)
 
@app.route('/coins')
def coins():
    return render_template('coins/coins.html', title='Coins')

@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    """
    Method to return bitcoin prediction data when a user clicks the bitcoin card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.date as date, T.price as Prediction, price_explain FROM mindsdb.bitcoin_model as T JOIN files.bitcoin_data as P WHERE P.Date > LATEST LIMIT 14')
    # create a dataframe for data from query
    btc_df = DataFrame.to_html(query.fetch(), index=False)
    return render_template('coins/bitcoin.html', query=query, btc_df=btc_df)

@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when a user clicks the ethereum card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.Date as Date, T.Close as Close, T.Open AS Open, T.High AS High, T.Low AS Low FROM mindsdb.eth_model as T JOIN files.Ethereum as P WHERE P.Date > LATEST LIMIT 14;')
    # create a dataframe for data from query
    eth_df = DataFrame.to_html(query.fetch(), index=False)

    return render_template('coins/ethereum.html', query=query, eth_df=eth_df)

if __name__ == '__main__':
    app.run(debug=True)
