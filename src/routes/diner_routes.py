from flask import Blueprint, jsonify, make_response, request
from ..controllers.diner_controller import get_all_restaurants, get_diner_restaurant_id, \
    get_diner_restaurant_dishes, get_diner_restaurant_dish, post_diner_dish_buy

diner = Blueprint('diner', __name__)

shopping_cart = []


@diner.route("/", methods=['GET'])
#muestra los restaurantes actuales
def diner_restaurant():
    restaurants = get_all_restaurants()
    return jsonify({
        "ok": True,
        "message": "Restaurants list",
        "data": restaurants
    }), 200


@diner.route("/<int:rid>", methods=['GET'])
#muestra informacion relevante del restaurant
def diner_restaurant_id(rid):
    restaurant = get_diner_restaurant_id(int(rid))
    return jsonify({
        "ok": True,
        "message": "Selected restaurant",
        "data": restaurant.name
    }), 200


@diner.route("/<int:rid>/dishes", methods=['GET'])
#muestra informacion de los platos del restaurant
def diner_restaurant_id_dishes(rid):
    dishes = get_diner_restaurant_dishes(int(rid))
    return jsonify({
        "ok": True,
        "message": "Restaurant's daily dishes",
        "data": dishes
    }), 200


@diner.route("/<int:rid>/dishes/<int:did>", methods=['POST'])
#muestra informacion de cada plato
#aqui tiene que añadirse el plato a una CESTA
def diner_restaurant_id_dish(rid, did):
    quantity = int(request.json.get("quantity"))
    dish = get_diner_restaurant_dish(int(rid), int(did))
    global shopping_cart
    shopping_cart.append({"id": int(did), "name": dish.name, "price": dish.price, "quantity": quantity})
    return jsonify({
        "ok": True,
        "message": "Dish saved in shopping cart",
        "dish": dish.name,
        "data": shopping_cart
    }), 200


@diner.route("/<int:rid>/dishes/buying", methods=['GET'])
#muestra informacion de cada plato y se pueda guardar en la cesta
def diner_restaurant_dish_buying(rid):
    dishes_buying = []
    global shopping_cart
    for cart in shopping_cart:
        post_diner_dish_buy(cart['name'],
                            float(cart['price']*cart['quantity']),
                            cart['quantity'],
                            int(rid), int(cart['id']))
        dishes_buying.append({"name": cart['name'],
                              "quantity": cart['quantity'],
                              "total price": float(cart['price']*cart['quantity'])})
    shopping_cart = []
    return jsonify({
        "ok": True,
        "message": "Purchased dishes",
        "data": dishes_buying
    }), 200
