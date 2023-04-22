from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class CoinForm(FlaskForm):
    coin = SelectField('Coin', choices=[('btcusd', 'Bitcoin'), ('ethusd', 'Ethereum'), ('ltcusd', 'Litecoin')], validators=[DataRequired()])
    input = SelectField('Input', choices=[('close_price', 'Close Price'), ('open_price', 'Open Price'), ('high_price', 'High Price'), ('low_price', 'Low Price'), ('volume', 'Volume')], validators=[DataRequired()])
    target = SelectField('Target', choices=[('close_price', 'Close Price'), ('open_price', 'Open Price'), ('high_price', 'High Price'), ('low_price', 'Low Price'), ('volume', 'Volume')], validators=[DataRequired()])
    submit = SubmitField('Get Prediction')
