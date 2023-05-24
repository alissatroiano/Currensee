from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired,  InputRequired, Length, Regexp, Email, EqualTo, Optional

class CoinForm(FlaskForm):
    coin = SelectField('Coin', choices=[('btcusd', 'Bitcoin'), ('ethusd', 'Ethereum'), ('ltcusd', 'Litecoin')], validators=[DataRequired()])
    submit = SubmitField('Get Prediction')

class register_form(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(8, 72)])
    cpwd = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("pwd", message="Passwords must match !"),
        ]
    )

class login_form(FlaskForm):
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    # Placeholder labels to enable form rendering
    username = StringField(
        validators=[Optional()]
    )