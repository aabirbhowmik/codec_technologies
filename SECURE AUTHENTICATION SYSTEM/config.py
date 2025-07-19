import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'a_very_secret_default_key_dont_use_in_prod')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'another_super_secret_jwt_key_dont_use_in_prod')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://auth_user:your_secure_password@localhost:5432/auth_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False