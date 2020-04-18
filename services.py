import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello Heroku"})

@app.route('/auth')
def authorization():
    auth     = request.authorization
    authType = request.args.get('by')

   # if authType=='google':
    return request.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=asdas')

    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
