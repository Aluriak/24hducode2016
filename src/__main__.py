"""
Entry point for the project.

usage:
    __main__.py [options]

options:
    --longitude=STRING      Longitude, as string
    --latitude=STRING       Latitude, as string

"""
import sys
import pickle
from docopt import docopt
from collections import namedtuple

from . import default
from . import tobject_factory
from . import source_factory
from . import source_tourinsoft
from .tobject import TObject


def tobjects_from_sources():
    print('Init Sources factory…', end='') ; sys.stdout.flush()
    sources = tuple(source_factory.all_sources())
    print('OK !\nInit TObjects factory…', end='') ; sys.stdout.flush()
    tobjects_factory = tobject_factory.TObjectFactory(sources)
    print('OK !\nRequest JSON data…', end='') ; sys.stdout.flush()
    init_data = source_tourinsoft.SourceTourinsoft().spawn_all()
    print('OK !\nProduce TObjects…', end='') ; sys.stdout.flush()
    tobjects = tuple(tobjects_factory.tobjects(init_data))
    print('OK !')
    return tuple(tobjects)

def gen_tobjects():
    """Get cached data in default.ALL_DATA_FILE file, or generate it"""
    try:
        with open(default.ALL_DATA_FILE, 'rb') as fd:
            tobjects        = pickle.load(fd)
            TObject.sources = pickle.load(fd)
    except IOError:
        print('No file ' + default.ALL_DATA_FILE + ' found. Data will be generated from databases')
        tobjects = tuple(tobjects_from_sources())
        with open(default.ALL_DATA_FILE, 'wb') as fd:
            pickle.dump(tobjects, fd)
            pickle.dump(TObject.sources, fd)
    return tobjects


# User definition
Position = namedtuple('User', ['latitude', 'longitude'])
args = docopt(__doc__)
user = Position(args['--latitude'], args['--longitude'])


# use tobjects here
tobjects = gen_tobjects()
print('##########################')
print(tobjects[0]['description'])
