from flask import Blueprint, jsonify, make_response, request
from ..controllers.diner_controller import get_all_restaurants

diner = Blueprint('diner', __name__)


@diner.route("/", methods=['GET'])
#muestra los restaurantes actuales
def diner_restaurant():
    restaurants = get_all_restaurants()
    print("restaurants => ", restaurants)
    return jsonify({
        "ok": True,
        "message": "Get restaurants"
    }), 200


@diner.route("/<int:rid>", methods=['GET'])
#muestra informacion relevante del restaurant
def diner_restaurant_id(rid):
    return jsonify({
        "ok": True,
        "message": "Get restaurant",
        "id_restaurant": rid
    }), 200


@diner.route("/<int:rid>/dishes", methods=['GET'])
#muestra informacion de los platos del restaurant
def diner_restaurant_id_dishes(rid):
    return jsonify({
        "ok": True,
        "message": "Get dishes",
        "id_restaurant": rid
    }), 200


@diner.route("/<int:rid>/dishes/<int:did>", methods=['GET'])
#muestra informacion de cada plato
def diner_restaurant_id_dish(rid, did):
    return jsonify({
        "ok": True,
        "message": "Get dish",
        "id_restaurant": rid,
        "id_dish": did
    }), 200


@diner.route("/<int:rid>/dishes/<int:did>/buying", methods=['POST'])
#muestra informacion de cada plato y se pueda guardar en la cesta
def diner_restaurant_dish_buying(rid, did):
    return jsonify({
        "ok": True,
        "message": "post dish buying",
        "id_restaurant": rid,
        "id_dish": did
    }), 200
