from __future__ import unicode_literals

import json

from seeuletter import api_requestor
from seeuletter.compat import string_type


def seeuletter_format(resp):
    types = {
        'letter': Letter,
        'postcard': Postcard
    }

    # Recursively Set Objects for Lists
    if isinstance(resp, dict) and 'object' in resp and resp['object'] == 'list':
        resp['data'] = [seeuletter_format(i) for i in resp['data']]
        return SeeuletterObject.construct_from(resp)
    if isinstance(resp, dict) and not isinstance(resp, SeeuletterObject):
        resp = resp.copy()
        if 'object' in resp and isinstance(resp['object'], string_type):
            klass = types.get(resp['object'], SeeuletterObject)
        else:
            klass = SeeuletterObject

        # Check For Arrays
        for key in resp:
            if isinstance(resp[key], list):
                resp[key] = [seeuletter_format(i) for i in resp[key]]
        return klass.construct_from(resp)
    else:
        return resp


class SeeuletterObject(dict):

    def __init__(self, id=None, **params):
        super(SeeuletterObject, self).__init__()
        if id:
            self['id'] = id

    @classmethod
    def construct_from(cls, values):
        instance = cls(values.get('id'))
        for k, v in values.items():
            instance[k] = seeuletter_format(v)
        return instance

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k)  

    def __setattr__(self, k, v):
        self[k] = v

    def __repr__(self):
        ident_parts = [type(self).__name__]

        if isinstance(self.get('object'), string_type):
            ident_parts.append(self.get('object'))

        if isinstance(self.get('id'), string_type):
            ident_parts.append('id=%s' % (self.get('id'),))

        unicode_repr = '<%s at %s> JSON: %s' % (
            ' '.join(ident_parts), hex(id(self)), str(self))

        return unicode_repr

    def __str__(self):
        return json.dumps(self, sort_keys=True, indent=2)


class APIResource(SeeuletterObject):
    @classmethod
    def retrieve(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s' % (cls.endpoint, id), params)
        return seeuletter_format(response)


# API Operations
class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, **params):
        for key, value in params.copy().items():
            if isinstance(params[key], dict):
                for subKey in value:
                    params[str(key) + '[' + subKey + ']'] = value[subKey]
                del params[key]
            elif isinstance(params[key], list):
                params[str(key) + '[]'] = params[key]
                del params[key]
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint, params)
        return seeuletter_format(response)


class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('post', cls.endpoint, params)
        return seeuletter_format(response)


class Letter(ListableAPIResource, CreateableAPIResource):
    endpoint = '/letters'

    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'from_address' in params:
                params['from'] = params['from_address']
                params.pop('from_address')
            if 'to_address' in params:
                params['to'] = params['to_address']
                params.pop('to_address')
        return super(Letter, cls).create(**params)


class Postcard(ListableAPIResource, CreateableAPIResource):
    endpoint = '/postcards'

    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'from_address' in params:
                params['from'] = params['from_address']
                params.pop('from_address')
            if 'to_address' in params:
                params['to'] = params['to_address']
                params.pop('to_address')
        return super(Postcard, cls).create(**params)

