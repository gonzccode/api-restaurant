from flask import Blueprint, jsonify, make_response, request
from ..controllers.diner_controller import get_all_restaurants, get_diner_restaurant_id, \
    get_diner_restaurant_dishes, get_diner_restaurant_dish, post_diner_dish_buy

diner = Blueprint('diner', __name__)

shopping_cart = []


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
    restaurant = get_diner_restaurant_id(int(rid))
    print("restaurant id => ", restaurant)
    return jsonify({
        "ok": True,
        "message": "Get restaurant",
        "id_restaurant": rid,
        "data": restaurant.name
    }), 200


@diner.route("/<int:rid>/dishes", methods=['GET'])
#muestra informacion de los platos del restaurant
def diner_restaurant_id_dishes(rid):
    dishes = get_diner_restaurant_dishes(int(rid))
    print("dishes => ", dishes)
    return jsonify({
        "ok": True,
        "message": "Get dishes of the day",
        "id_restaurant": rid
        #para data agregar un list comprehions y asi tener como reusltado el array con los objetos
    }), 200


@diner.route("/<int:rid>/dishes/<int:did>", methods=['GET'])
#muestra informacion de cada plato
#aqui tiene que añadirse el plato a una CESTA
def diner_restaurant_id_dish(rid, did):
    dish = get_diner_restaurant_dish(int(rid), int(did))
    global shopping_cart
    shopping_cart.append({dish.id, dish.name, dish.price, dish.is_active_day})
    print("shopping_cart => ", shopping_cart)
    return jsonify({
        "ok": True,
        "message": "Get dish",
        "id_restaurant": rid,
        "id_dish": did,
        "data": dish.name
    }), 200


@diner.route("/<int:rid>/dishes/<int:did>/buying", methods=['POST'])
#muestra informacion de cada plato y se pueda guardar en la cesta / QUITAR EL INT_DID
#solo es /<int:rid>/dishes/buying
def diner_restaurant_dish_buying(rid, did):
    quantity = int(request.json.get("quantity"))
    dish = get_diner_restaurant_dish(int(rid), int(did))
    #RECORRER EL ARRAY DE SHOPPING CART Y SACAR LAS VARIALES PARA GUARDAR Y LUEGO LIMPIAR EL CARRITO
    post_diner_dish_buy(dish.name, int(dish.price*quantity), quantity, int(rid), int(did))
    global shopping_cart
    shopping_cart = []
    return jsonify({
        "ok": True,
        "message": "post dish buying",
        "id_restaurant": rid,
        "id_dish": did
    }), 200
