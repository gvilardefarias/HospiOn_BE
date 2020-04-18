import requests
import jwt
import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import methods

app = Flask(__name__)
CORS(app)

secretWorld = "biiirHospOn"

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello Heroku"})

@app.route('/auth', methods=['GET'])
def authorizationGoogle():
    auth     = request.authorization
    authType = request.args.get('by')

    if authType=='google':
        r    = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + str(auth))
        data = r.json()

        if r.status_code==200:
            email = data['email']

            data['token'] = jwt.encode({'email': email}, secretWorld, algorithm='HS256')

            if not methods.userRegistered(email):
                methods.register(data['given_name'], data['family_name'], email, "PF")
    
            return jsonify(data)


    return jsonify({"message": "Authentication Failed"}), 400

@app.route('/auth', methods=['POST'])
def authorizationFacebook():
    auth     = request.authorization
    authType = request.args.get('by')

    content  = request.json

    if authType=='facebook':
        data = r.json()

        if r.status_code==200:
            r    = requests.get('https://graph.facebook.com/me?access_token=' + str(auth))
            email = content['email']

            data['token'] = jwt.encode({'email': email}, secretWorld, algorithm='HS256')

            if not methods.userRegistered(email):
                methods.register(data['name'], '', email, "PF")
    
            return jsonify(data)

    return jsonify({"message": "Authentication Failed"}), 400
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
