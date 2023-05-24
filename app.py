import os
from flask import Flask, render_template, request
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm
import pandas as pd
from pandas import DataFrame
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

from models import User
# Flask Login
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"
# import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'login'

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager.init_app(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager.init_app(app)

server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)
import mindsdb_sdk


@app.route('/')
def index():
    return render_template('index.html', title='Home')

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)

def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email already registered!")

def validate_uname(self, uname):
    if User.query.filter_by(username=username.data).first():
        raise ValidationError("Username already taken!")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Login route
@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    return render_template("auth.html",form=form)

# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()

    return render_template("auth.html",form=form)
 

@app.route('/coins')
def coins():
    return render_template('coins.html', title='Coins')


@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    """
    Method to return bitcoin prediction data when a user clicks the bitcoin card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.Date as Date, T.Close as Close FROM mindsdb.eth_1 as T JOIN files.Ethereum as P WHERE P.Date > LATEST LIMIT 14;')
    # create a dataframe for data from query
    eth_df = DataFrame.to_html(query.fetch(), index=False)
    return render_template('bitcoin.html')


@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when a user clicks the ethereum card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.Date as Date, T.Close as Close, T.Open AS Open, T.High AS High, T.Low AS Low FROM mindsdb.eth_model as T JOIN files.Ethereum as P WHERE P.Date > LATEST LIMIT 14;')
    # create a dataframe for data from query
    eth_df = DataFrame.to_html(query.fetch(), index=False)

    return render_template('ethereum.html', query=query, eth_df=eth_df)


# @app.route('/login', methods=['GET', 'POST'])
# def login():


if __name__ == '__main__':
    app.run(debug=True)
