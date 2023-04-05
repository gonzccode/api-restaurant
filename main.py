from flask import Flask, make_response, request
from src.routes.restaurant_routes import restaurant

app = Flask(__name__)

app.register_blueprint(restaurant)
#app.register_blueprint(restaurant, url_prefix='/session')


@app.route("/", methods=['GET', 'POST'])
def dishes():
    if request.method == 'GET':
        return "get dishes"

