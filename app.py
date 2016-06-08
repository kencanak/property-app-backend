from eve import Eve
from eve.auth import BasicAuth
import hashlib, uuid
from flask import Flask
from flask import jsonify
from flask import request
from settings import JWT_SECRET
import jwt
from eve.auth import TokenAuth
import datetime
import os
from flask.ext.cors import CORS


# Heroku support: bind to PORT if defined, otherwise default to 5000.
if os.environ.get('PORT'):
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

def generate_salt():
    return uuid.uuid4().hex

def sanitize_user_credential(user):
    user['salt'] = generate_salt()
    user['password'] = hashlib.sha512(user['password'] + user['salt']).hexdigest()
    return user

def before_insert_user(users):
    for user in users:
        user = sanitize_user_credential(user)

def before_update_user(updates, original):
    user = sanitize_user_credential(updates)

def decoding_jwt(token):
    return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])


class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        """For the purpose of this example the implementation is as simple as
        possible. A 'real' token should probably contain a hash of the
        username/password combo, which sould then validated against the account
        data stored on the DB.
        """
        # decodedToken = decoding_jwt(token);
        tokenData = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        accounts = app.data.driver.db['user']
        account = accounts.find_one({'email': tokenData['email']})
        userPass = hashlib.sha512(request.json['password'] + account['salt']).hexdigest()
        if (account and account['password'] == userPass):
            return account
        else:
            return jsonify({"result":"failed","message": "invalid token"})



app = Eve(settings='settings.py', auth=TokenAuth)
app.on_insert_user += before_insert_user
app.on_update_user += before_update_user
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/authenticate', methods=['POST'])
@cross_origin()
def authenticate():
    accounts = app.data.driver.db['user']
    account = accounts.find_one({'email': request.json['email']})

    userPass = hashlib.sha512(request.json['password'] + account['salt']).hexdigest()
    if (account and account['password'] == userPass):
        encoded = jwt.encode({'password': request.json['password'], 'email': account['email'], 'timestamp':  str(datetime.datetime.now().time())}, JWT_SECRET, algorithm='HS256')
        return jsonify({"result": "success","token":encoded.decode('unicode_escape')})
    else:
        return jsonify({"result":"failed","message":"authentication failed"})


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
