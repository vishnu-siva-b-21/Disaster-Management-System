import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "secret_key"
    MONGO_URI = (
        os.getenv("MONGO_URI") or "mongodb://localhost:27017/disaster_management"
    )
