from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, ValidationError
from app.models import User


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Create Account")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already taken. Please choose another.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already registered. Please log in.")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Keep me logged in")
    submit = SubmitField("Sign In")


class TaskForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired(), Length(max=200)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=1000)])
    priority = SelectField("Priority", choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")], default="medium")
    category = StringField("Category", validators=[Optional(), Length(max=50)])
    due_date = DateField("Due Date", validators=[Optional()])
    submit = SubmitField("Save Task")
