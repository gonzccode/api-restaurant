from flask import Blueprint, make_response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, set_access_cookies
from ..controllers.restaurant_controller import login_user, register_user, \
    register_restaurant, add_dish, update_dish, delete_dish, get_dish, get_dishes
from ..utils.encrypt import create_hashed_password, validate_password
from ..utils.token import generate_token

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
    id_user_db, password_db = login_user(username)
    print("/login =>", id_user_db, password_db)
    login_value = validate_password(str(password), str(password_db))

    if login_value:
        token = generate_token(id_user_db)
        response = jsonify({"login": True, "token": token})
        set_access_cookies(response, token)
        # return jsonify({'message': 'Invalid username or password'}), 401
        #return make_response('Successful login', 200)
        return response, 200

    else:
        # return jsonify({'message': 'Invalid username or password'}), 401
        return make_response('Unable to login', 403, {'Status': 'Invalid credentials'})


@restaurant.route("/session/restaurant", methods=['POST'])
#@jwt_required()
def session_restaurant():
    user_id = get_jwt_identity()
    print("user id jwt =>", user_id)
    name_restaurant = request.json.get('name')
    #register_restaurant(name_restaurant, user_id)
    #register_restaurant(name_restaurant, 1)
    return make_response('Successful registration restaurant', 200)


#@restaurant.route("/session/restaurant/:id/dish")
@restaurant.route("/session/restaurant/<int:rid>/dish", methods=['POST'])
#jwt_required
def session_restaurant_add_dish(rid):
    name_dish = request.json.get('name')
    price_dish = request.json.get('price')
    url_dish = request.json.get('url')
    status_dish = request.json.get('status')
    #name_restaurant = request.json.get('restaurant')
    print("id params ", rid)
    add_dish(name_dish, price_dish, url_dish, status_dish, rid)
    return make_response('Successful add dish', 200)


@restaurant.route("/session/restaurant/<int:rid>/dish/<int:did>", methods=['GET', 'PUT', 'DELETE'])
#@jwt_required()
def session_restaurant_update_dish(rid, did):
    if request.method == 'PUT':
        name_dish = request.json.get('name')
        price_dish = request.json.get('price')
        url_dish = request.json.get('url')
        status_dish = request.json.get('is_active_day')
        update_dish(str(name_dish), int(price_dish), str(url_dish), int(status_dish), int(rid), int(did))
        return make_response('Successful update dish', 200)
    elif request.method == 'DELETE':
        delete_dish(int(rid), int(did))
        return make_response('Successful delete dish', 200)
    else:
        dish = get_dish(int(rid), int(did))
        return make_response('Successful get dish', 200)


@restaurant.route("/session/restaurant/<int:rid>/dishes", methods=['GET'])
#@jwt_required()
def session_restaurant_get_dishes(rid):
    dishes = get_dishes(int(rid))
    return make_response('Successful get dishes', 200)