from flask import Flask
from flask_jwt_extended import create_access_token

app = Flask(__name__)


def generate_token(user_id):
    token = create_access_token(identity=int(user_id))
    print("token: ", token)
    return token
