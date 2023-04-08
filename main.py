from flask import Flask, make_response, request
from flask_jwt_extended import JWTManager
from src.routes.restaurant_routes import restaurant
from src.routes.diner_routes import diner

app = Flask(__name__)

app.config['SECRET_KEY'] = '26b1dedd2a4841e8a18be98c5a9a38c7'

app.register_blueprint(restaurant)
app.register_blueprint(diner, url_prefix="/restaurants")


@app.route("/", methods=['GET'])
def dishes():
    if request.method == 'GET':
        return make_response("WELCOME RESTAURANT API", 200)
