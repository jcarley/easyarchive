import datetime
import json

import dateutil.parser


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'type': 'datetime',
                'data': obj.isoformat()
            }
        if isinstance(obj, datetime.date):
            return {
                'type': 'date',
                'data': obj.isoformat()
            }
        return super(JSONEncoder, self).default(obj)


class JSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('object_hook', self.default_object_hook)
        super(JSONDecoder, self).__init__(*args, **kwargs)

    def default_object_hook(self, obj):
        if 'type' in obj and 'data' in obj:
            if obj['type'] == 'datetime':
                return dateutil.parser.parse(obj['data'])
            if obj['type'] == 'date':
                return dateutil.parser.parse(obj['data']).date()
        return obj


def dumps(*args, **kwargs):
    kwargs.setdefault('cls', JSONEncoder)
    return json.dumps(*args, **kwargs)


def loads(*args, **kwargs):
    kwargs.setdefault('cls', JSONDecoder)
    return json.loads(*args, **kwargs)
