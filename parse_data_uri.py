import re
from base64 import urlsafe_b64decode

DATA_URI_REGEX = (r'data:' + r'(?P<mimetype>[\w]+\/[\w\-\+\.]+)?' + r'(\;charset\=(?P<charset>)[\w\-\+\.]+)?' + r'(\;(?P<base64>base64))?' + r',(?P<data>.*)')

class DataURI(object):

    def __init__(self, data_uri):
        self._uri = str(data_uri)
        self._mimetype, self._charset, self._data = self._parse(self._uri)

    def __repr__(self):
        return str({'uri': self._uri,
                    'mimetype': self._mimetype,
                    'charset': self._charset,
                    'data': self._data})

    @property
    def mimetype(self):
        return self._mimetype

    @property
    def charset(self):
        return self._charset

    @property
    def data(self):
        return self._data

    def _parse(self, data_str):
        match = re.match(DATA_URI_REGEX, data_str)
        if not match:
            raise ValueError('Not a valid data uri: %r' % data_str)

        parsed_data = match.groupdict()
        if parsed_data['base64']:
            decoded_data = urlsafe_b64decode(parsed_data['data'])
        else:
            raise ValueError('Resource is not base64 encoded: %r' % data_str)

        return parsed_data['mimetype'], parsed_data['charset'], decoded_data

