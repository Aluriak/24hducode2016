"""
Entry point for the project.

"""
import sys
import pickle

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
    json = source_tourinsoft.SourceTourinsoft().spawn_all()
    print('OK !\nProduce TObjects…', end='') ; sys.stdout.flush()
    tobjects = tobjects_factory.tobjects(json)
    print('OK !')
    TObject.sources = tuple(sources)
    return tuple(TObject(tobject) for tobject in tobjects)

def gen_tobjects():
    """Get cached data in default.ALL_DATA_FILE file, or generate it"""
    try:
        with open(default.ALL_DATA_FILE, 'rb') as fd:
            tobjects = pickle.load(fd)
    except IOError:
        print('No file ' + default.ALL_DATA_FILE + ' found. Data will be generated from databases')
        tobjects = tuple(tobjects_from_sources())
        with open(default.ALL_DATA_FILE, 'wb') as fd:
            pickle.dump(tobjects, fd)
    return tobjects

# use tobjects here
tobjects = gen_tobjects()
print('##########################')
print(tobjects[0]['description'])
