from flask import Flask, make_response, request
from flask_jwt_extended import JWTManager
from src.routes.restaurant_routes import restaurant
from src.routes.diner_routes import diner

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'

jwt = JWTManager(app)

app.register_blueprint(restaurant)
app.register_blueprint(diner, url_prefix="/restaurants")


@app.route("/", methods=['GET'])
def dishes():
    if request.method == 'GET':
        return "WELCOME RESTAURANT API"

