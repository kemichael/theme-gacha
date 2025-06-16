from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()

def init_db(app: Flask):
    user = os.environ.get("DB_USER", "user")
    password = os.environ.get("DB_PASSWORD", "password")
    host = os.environ.get("DB_HOST", "localhost")
    dbname = os.environ.get("DB_NAME", "isekai_gacha")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{password}@{host}/{dbname}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)