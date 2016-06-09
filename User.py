userSchema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'email': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 30,
        'required': True,
        'unique': True
    },
    'first_name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'last_name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True
    },
    'password': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 21,
        'required': True
    },
    'salt': {
        'type': 'string'
    }
}

user = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'user',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'first_name'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST', 'DELETE'],

    'schema': userSchema,
    'datasource': {
        'projection': {
            'password': 0,
            'salt': 0
        }
    },
    'public_methods': ['GET','POST'],
    'public_item_methods': ['GET','POST'],
    'X_DOMAINS': '*'
}
