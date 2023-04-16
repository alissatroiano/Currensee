from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class CoinForm(FlaskForm):
    coin = SelectField('Coin', choices=[('btcusd', 'Bitcoin'), ('ethusd', 'Ethereum'), ('ltcusd', 'Litecoin')], validators=[DataRequired()])
    submit = SubmitField('Get Prediction')