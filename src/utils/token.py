from flask import Flask, request, jsonify, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = '26b1dedd2a4841e8a18be98c5a9a38c7'


def generate_token(user_id, username):
    token = jwt.encode({
        'id_user': user_id,
        'username': username,
        'expiration': str(datetime.utcnow() + timedelta(hours=2))
    }, app.config['SECRET_KEY'], algorithm="HS256")
    response = jsonify({'token': token})
    session['token'] = token
    return response


def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'token' in session:
           token = session['token']

       print("decorator token => ", token)

       if not token:
          return jsonify({'message': 'Missing valid token'}), 401

       try:
           print("try token => ", token)
           data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
           data_user_token = {
               "id_user": data['id_user'],
               "username": data['username']
           }
           return f(data_user_token, *args, **kwargs)
       except Exception as error:
          return jsonify({'message': 'Token is invalid', 'error': error}), 401
   return decorator
