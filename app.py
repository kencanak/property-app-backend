from eve import Eve
from eve.auth import BasicAuth
import hashlib, uuid
from flask import Flask
from flask import jsonify
from flask import request
from settings import JWT_SECRET, JWT_ISSUER
import datetime
import jwt


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
    print get_request_auth_value()
    user = sanitize_user_credential(updates)

def decoding_jwt(token):
    return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])




app = Eve(settings='settings.py', auth=JWTAuth)
app.on_insert_user += before_insert_user
app.on_update_user += before_update_user

@app.route('/authenticate', methods=['POST'])
def authenticate():
    accounts = app.data.driver.db['user']
    account = accounts.find_one({'email': request.json['email']})

    userPass = hashlib.sha512(request.json['password'] + account['salt']).hexdigest()
    if (account and account['password'] == userPass):
        encoded = jwt.encode({'password': account['password'], 'email': account['email'], 'timestamp':  str(datetime.datetime.now().time())}, JWT_SECRET, algorithm='HS256')
        import base64
        print 'Basic ' + str(base64.b64encode(encoded + ':'))

        return jsonify({"result": "success","token":encoded.decode('unicode_escape')})
    else:
        return jsonify({"result":"failed","message":"authentication failed"})


if __name__ == '__main__':
    app.run(debug=True)
