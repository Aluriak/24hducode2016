"""
Definition of sources factory.

Automatic import of any source.Source subclass,
in any subpackage with name beginning with 'source_'

"""
import importlib
import glob
import os

from .info    import PACKAGE_NAME, PACKAGE_VERSION
from .default import SUBMODULES_SOURCES_PREFIX
from .source  import Source

# from .source_tourinsoft import SourceTourinsoft
from .source_weather import SourceWeather
from .source_wkpd import WikiSource


def all_sources():
    return (
        # SourceTourinsoft(),
        # SourceWeather(),
        # WikiSource(),
    )

# def source_class_check(cls):
    # """Return True iff given cls is a valid source class"""
    # return (
        # issubclass(cls.__class__, type) and  # its a class
        # issubclass(cls, Source) and  # its a source
        # cls is not Source  # but not Source itself
    # )


# def import_classes(module_names, class_check=source_class_check):
    # """Yields all Source subclasses found in package directory"""
    # for module_name in module_names:
        # print('MODULE NAME:', module_name)
        # module = importlib.import_module(module_name, package=PACKAGE_NAME)
        # print('MODULE:', module)
        # attributes = (module.__getattribute__(_) for _ in module.__dir__())
        # yield from (attr for attr in attributes if class_check(attr))


# def list_submodules(prefix=SUBMODULES_SOURCES_PREFIX):
    # """Return generator of plugin names that are detected and importables."""
    # return (f[:-3].replace('/', '.')
            # for f in glob.glob(PACKAGE_NAME + '/*.py')
            # if not f.startswith('_')
           # )


# print('###########################################')
# submods = tuple(list_submodules())
# print('SUBMODS:', submods)
# classes = tuple(import_classes(submods))
# print('FOUND CLASSES:', classes)


# print('###########################################')
