__author__ = 'Tom Van den Eede'
__copyright__ = 'Copyright 2018-2022, Palette2 Splicer Post Processing Project'
__credits__ = ['Tom Van den Eede',
               'Tim Brookman'
               ]
__license__ = 'GPLv3'
__maintainer__ = 'Tom Van den Eede'
__email__ = 'P2PP@pandora.be'

import platform

MASTER = "https://github.com/tomvandeneede/p2pp/raw/master/version.py"

_p = platform.python_version().strip()
python_version = _p[0]

# SECTION get_version


def get_version(_url_):

    try:
        import urllib.request
        import ssl
        https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext())
        opener = urllib.request.build_opener(https_sslv3_handler)
        urllib.request.install_opener(opener)
        response = opener.open(_url_).read().decode('utf-8')
        lines = "".join(response).splitlines()

        # get version information
        _maj = -1
        _min = -1
        _bld = -1

        for line in lines:
            if line.startswith("MajorVersion"):
                _maj = int(line[line.find("=")+1:])
            if line.startswith("MinorVersion"):
                _min = int(line[line.find("=")+1:])
            if line.startswith("Build"):
                _bld = int(line[line.find("=")+1:])

        if _maj == -1 or _min == -1 or _bld == -1:
            return None

        return "{}.{:02}.{:03}".format(_maj, _min, _bld)
    except:
        return "0.0"
