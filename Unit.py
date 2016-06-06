unitSchema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'address': {
        'type': 'dict',
        'schema': {
            'block_number': {
                'type': 'string',
                'required': True
            },
            'street_name': {
                'type': 'string',
                'required': True
            },
            'postal_code': {
                'type': 'integer',
                'max': 999999
            },
            'city': {
                'type': 'string',
                'required': True
            },
            'country': {
                'type': 'string',
                'required': True
            },
            'coordinates': {
                'type': 'dict',
                'schema': {
                    'lat': {
                        'type': 'float',
                        'required': True
                    },
                    'lon': {
                        'type': 'float',
                        'required': True
                    }
                }
            }
        }
    },
    'price': {
        'type': 'float',
        'required': True
    },
    'num_rooms': {
        'type': 'integer',
        'required': True,
        'max': 10
    },
    'num_bathrooms': {
        'type': 'integer',
        'required': True,
        'max': 10
    },
    'sqft': {
        'type': 'float',
        'required': True
    }
}

unit = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'unit',


    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST', 'DELETE'],

    'schema': unitSchema
}
