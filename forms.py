from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class BitcoinForm(FlaskForm):
    coin = SelectField('Coin', choices=[('BTC', 'Bitcoin'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin')], validators=[DataRequired()])
    submit = SubmitField('Get Prediction')