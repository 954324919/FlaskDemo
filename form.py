from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
class LoginForm(Form):
    username=StringField(validators=[DataRequired()])
    password=PasswordField(validators=[DataRequired()])
    submit=SubmitField()
