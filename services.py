import requests
import time
from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import methods

app = Flask(__name__)
CORS(app)

instanceJWT = JWT()
key = jwk_from_dict({'kty': 'oct', 'k': 'biiirHospOn'})

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello Heroku"})

@app.route('/auth', methods=['POST'])
def authorization():
    authType = request.args.get('by')

    content  = request.json

    if authType=='facebook':
        auth     = request.headers['authorization']
        r    = requests.get('https://graph.facebook.com/me?access_token=' + str(auth))
        data = r.json()

        if r.status_code==200:
            email = content['email']

            data['token'] = instanceJWT.encode({'email': email, 'time': time.time()}, key, alg='HS256')

            if not methods.userRegistered(email):
                methods.register(data['name'], '', email, "PF")

            return jsonify(data)
    elif authType=='google':
        auth     = request.headers['authorization'].split()[1]
        r    = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?access_token=' + str(auth))
        data = r.json()
        print(data)
        print('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + str(auth))

        if r.status_code==200:
            email = content['email']

            data['token'] = instanceJWT.encode({'email': email, 'time': time.time()}, key, alg='HS256')

            if not methods.userRegistered(email):
                methods.register(data['given_name'], data['family_name'], email, "PF")
    
            return jsonify(data)
    elif authType=='cnpj':
        email = content['email']

        data = {}
        data['token'] = instanceJWT.encode({'email': email, 'time': time.time()}, key, alg='HS256')

        if not methods.userRegistered(email):
            methods.registerPJ(content['name'], email, content['password'], content['cnpj'])
        else:
            return jsonify({"message": "Register already exists"}), 400

        return jsonify(data)

    return jsonify({"message": "Authentication Failed"}), 400

@app.route('/login', methods=['POST'])
def login():
    content  = request.json

    email = content['email']

    if methods.login(email, content['password']):
        data = {}
        data['token'] = instanceJWT.encode({'email': email, 'time': time.time()}, key, alg='HS256')

        return jsonify(data)

    return jsonify({"message": "Authentication Failed"}), 400

    
@app.route('/user/<email>')
def getUser(email):
    return jsonify(methods.getUser(email))

@app.route('/hospital/<ID>')
def getHospital(ID):
    return jsonify(methods.getHospital(ID))

@app.route('/getAllHospital/')
def getAllHospital():
    return jsonify(methods.getAllHospital())

@app.route('/getOrder/<ID>')
def getOrder(ID):
    return jsonify(methods.getOrder(ID))

@app.route('/getAllOrders/')
def getAllOrders():
    return jsonify(methods.getAllOrders())

@app.route('/updateOrder/<ID>', methods=['POST'])
def updateOrder(ID):
    return jsonify(methods.updateOrder(ID, request.json))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
