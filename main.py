from flask import Flask, make_response, request
from src.controllers.restaurant_controller import register_user, login_user
from src.utils.encrypt import create_hashed_password, validate_password

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def dishes():
    if request.method == 'GET':
        return "get dishes"


@app.route("/register", methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    new_password = create_hashed_password(password)
    register_user(str(username), str(new_password))
    return make_response('Successful registration', 200)


@app.route("/login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    password_db = login_user(username)
    login_value = validate_password(str(password), str(password_db))

    if login_value:
        return make_response('Successful login', 200)
    else:
        return make_response('Unable to login', 403, {'Status': 'Invalid credentials'})
