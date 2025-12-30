import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = 'car price api'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY','secret_key')
    API_KEY = os.get('API_KEY','DEMO_KEY')
    JWT_ALGORITHM = 'HSE256'
    MODEL_PATH = 'app/models/model.pkl'
    REDIS_URL = os.getenv('REDIS_URL','redis://localhost:6379')


settings = Settings()