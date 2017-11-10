import sys


if sys.version_info[0] == 3:  
    string_type = str
    from io import BytesIO
else:  
    string_type = basestring
    from StringIO import StringIO as BytesIO
