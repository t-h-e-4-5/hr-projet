from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] = "srdtfghjiklm"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://theophile:123456789@localhost/hr-db"

db = SQLAlchemy(app)