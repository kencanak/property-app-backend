import os
from User import user
from Unit import unit

# We want to run seamlessly our API both locally and on Heroku, so:
if os.environ.get('PORT'):
    # We're hosted on Heroku! Use the MongoHQ sandbox as our backend.
    MONGO_HOST = 'ds025583.mlab.com'
    MONGO_PORT = 25583
    MONGO_USERNAME = 'propertyapp'
    MONGO_PASSWORD = 'propertyapp'
    MONGO_DBNAME = 'property-app'
else:
    # Running on local machine. Let's just use the local mongod instance.

    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    # MONGO_USERNAME = 'user'
    # MONGO_PASSWORD = 'user'
    MONGO_DBNAME = 'property-app-backend'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

JWT_SECRET = 'flaskisawesome'
JWT_ISSUER = 'apes'

DOMAIN = {'user': user,'unit': unit}
