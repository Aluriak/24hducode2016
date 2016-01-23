"""
Entry point for the project.

"""
import sys

# from . import tourinsoft_api
from . import tobject_factory
from . import source_factory


print('Init Sources factory…', end='') ; sys.stdout.flush()
sources = source_factory.all_sources()
print('OK !\nInit TObjects factory…', end='') ; sys.stdout.flush()
tobjects_factory = tobject_factory.TObjectFactory(sources)
print('OK !\nRequest JSON data…', end='') ; sys.stdout.flush()
json = tourinsoft_api.request()
print('OK !\nProduce TObjects…', end='') ; sys.stdout.flush()
tobjects = tobjects_factory.tobjects(json)
print('OK !')

print(tobjects)
