from __future__ import unicode_literals


class SeeuletterError(Exception):

    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None):
        super(SeeuletterError, self).__init__(message)
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body


class APIError(SeeuletterError):
    pass


class APIConnectionError(SeeuletterError):
    pass


class AuthenticationError(SeeuletterError):
    pass


class InvalidRequestError(SeeuletterError):
    pass
