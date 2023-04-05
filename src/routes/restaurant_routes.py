from flask import Blueprint, make_response, request
from ..controllers.restaurant_controller import login_user, register_user
from ..utils.encrypt import create_hashed_password, validate_password

restaurant = Blueprint('restaurant', __name__)


@restaurant.route("/register", methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    new_password = create_hashed_password(password)
    register_user(str(username), str(new_password))
    return make_response('Successful registration', 200)


@restaurant.route("/login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    password_db = login_user(username)
    login_value = validate_password(str(password), str(password_db))

    if login_value:
        return make_response('Successful login', 200)
    else:
        return make_response('Unable to login', 403, {'Status': 'Invalid credentials'})