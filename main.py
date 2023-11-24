from flask import Flask
import jinja2
from flask_sqlalchemy import SQLAlchemy
from route.region import fetch
from route.tax_param_route import tax
from route.tax_route import calc
from dbsef import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length



app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/lab3'
app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False
db.init_app(app)
app.register_blueprint(fetch)
app.register_blueprint(tax)
app.register_blueprint(calc)
if __name__ == "__main__":
    app.run(debug=True)
