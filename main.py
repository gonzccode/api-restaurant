from flask import Flask, request
from src.controllers.restaurant_controller import create_user, login

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def dishes():
    if request.method == 'GET':
        return "get dishes"


#create_user('gonzcca', '123456')

login('gonzcca', '123456')
#if __name__ == '__main__':
#    pass
