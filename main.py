from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def dishes():
    if request.method == 'GET':
        return "get dishes"
