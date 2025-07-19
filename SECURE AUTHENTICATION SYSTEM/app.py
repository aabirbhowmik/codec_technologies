from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

import routes

if __name__ == '__main__':
    with app.app_context():
        # Create database tables based on models.py
        db.create_all()
    app.run(debug=True) # Set debug=False in production!