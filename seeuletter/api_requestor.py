from __future__ import unicode_literals

import requests

import seeuletter
from seeuletter import error
from seeuletter.version import VERSION


def _is_file_like(obj):
    # https://stackoverflow.com/questions/1661262/check-if-object-is-file-like-in-python
    return hasattr(obj, 'read') and hasattr(obj, 'seek')


class APIRequestor(object):
    def __init__(self, key=None):
        self.api_key = key or seeuletter.api_key

    def parse_response(self, resp):
        if resp.status_code == 504:
            raise error.APIConnectionError(resp.content or resp.reason,  
                                           resp.content, resp.status_code, resp)

        payload = resp.json()
        if resp.status_code == 200:
            return payload
        elif resp.status_code == 401:
            raise error.AuthenticationError(payload['error']['message'],
                                            resp.content, resp.status_code, resp)
        elif resp.status_code in [404, 422]:
            raise error.InvalidRequestError(payload['error']['message'],
                                            resp.content, resp.status_code, resp)
        else:  
            raise error.APIError(payload['error']['message'], resp.content, resp.status_code, resp)

    def request(self, method, url, params=None):
        headers = {
            'User-Agent': 'Seeuletter/v1 PythonBindings/%s' % VERSION
        }

        if hasattr(seeuletter, 'api_version'):
            headers['Seeuletter-Version'] = seeuletter.api_version

        if params and 'headers' in params:
            headers.update(params['headers'])
            del params['headers']

        if method == 'get':
            return self.parse_response(
                requests.get(seeuletter.api_base + url, auth=(self.api_key, ''), params=params, headers=headers)
            )
        elif method == 'delete':
            return self.parse_response(
                requests.delete(seeuletter.api_base + url, auth=(self.api_key, ''), headers=headers)
            )
        elif method == 'post':
            data = {}
            files = params.pop('files', {})
            explodedParams = {}

            for k, v in params.items():
                if isinstance(v, dict) and not isinstance(v, seeuletter.resource.SeeuletterObject):
                    for k2, v2 in v.items():
                        explodedParams[k + '[' + k2 + ']'] = v2
                else:
                    explodedParams[k] = v

            for k, v in explodedParams.items():
                if _is_file_like(v):
                    files[k] = v
                else:
                    if isinstance(v, seeuletter.resource.SeeuletterObject):
                        data[k] = v.id
                    else:
                        if isinstance(v, dict):
                            for k2, v2 in v.items():
                                data[k + '[' + k2 + ']'] = v2
                        else:
                            data[k] = v

            return self.parse_response(
                requests.post(seeuletter.api_base + url, auth=(self.api_key, ''), data=data, files=files, headers=headers)
            )
