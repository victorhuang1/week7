from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required

class RegisterForm(FlaskForm):
    username=StringField('Yonghuming',validators=[Required(),Length(3,24)])
    email=StringField('Youxiang',validators=[Required(),Email()])
    password=PasswordField('Mima',validators=[Required(),Length(6,24)])
    repeat_password=PasswordField('ReMima',validators=[Required(),EqualTo('password')])
    submit=SubmitField('Tijiao')

class LoginForm(FlaskForm):
    email=StringField('Youxiang',validators=[Required(),Email()])
    password=PasswordField('Mima',validators=[Required(),Length(6,24)])
    remember_me=BooleanField('Jizhuwo')
    submit=SubmitField('Tijiao')
