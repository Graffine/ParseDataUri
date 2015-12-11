import re
from base64 import urlsafe_b64encode, urlsafe_b64decode

MIMETYPE_REGEX_PATTERN = (r'(?P<mimetype>[\w]+\/[\w\-\+\.]+)?')
MIMETYPE_REGEX_OBJ = re.compile(r'^' + MIMETYPE_REGEX_PATTERN + r'$')

CHARSET_REGEX_PATTERN = (r'(\;charset\=(?P<charset>)[\w\-\+\.]+)?' )
CHARSET_REGEX_OBJ = re.compile(r'^' + CHARSET_REGEX_PATTERN + r'$')

DATA_URI_REGEX = (r'data:' + MIMETYPE_REGEX_PATTERN + CHARSET_REGEX_PATTERN + r'(\;(?P<base64>base64))?' + r',(?P<data>.*)')

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

    @classmethod
    def formatter(cls, mimetype='text/plain', charset='us-ascii', data=None):
        pattern = 'data:'
        if mimetype is not None:
            if MIMETYPE_REGEX_OBJ.match(str(mimetype)) is None:
                raise ValueError('Invalid mimetype: %r' % mimetype)
            pattern = '%s%s' % (pattern, mimetype)

        if charset is not None:
            if CHARSET_REGEX_OBJ.match((';charset=%s' % charset)) is None:
                raise ValueError('Invalid charset: %r' % charset)
            pattern = '%s;charset=%s' % (pattern, charset)

        if data is None:
            raise ValueError('Data should not be none')

        encoded_data = urlsafe_b64encode(data)
        pattern = '%s;base64,%s' % (pattern, encoded_data)

        return pattern

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
