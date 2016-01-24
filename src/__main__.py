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
from src.visualisation.distance import distance_gps
from PIL import Image, ImageDraw, ImageFont # pip install pillow

from . import default
from . import tobject_factory
from . import source_factory
from . import source_tourinsoft
from .tobject import TObject
from .visualisation import make_map


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
user = Position(float(args['--latitude']), float(args['--longitude']))
if user.latitude is None:
    user.latitude = -0.07
if user.longitude is None:
    user.latitude = 47.70

# use tobjects here
tobjects = gen_tobjects()
# from src.visualisation import format_types_data as fca
# fca.lattice(tobjects)
# print('##########################')
# print(tobjects[0])
# exit()


def pretiffy(string, wordsize=12):
    return ' '.join(
        ('\n'+word) if idx % wordsize == 0 else word
        for idx, word in enumerate(string.split())
    )


def gen_wanteds(tobjects):
    filtereds = (o for o in tobjects if default.FIELD_LATITUDE in o)
    for i, tobject in enumerate(filtereds):
        lat1 = tobject[default.FIELD_LATITUDE]
        lon1 = tobject[default.FIELD_LONGITUDE]
        if distance_gps((float(lon1), float(lat1)),
                        (user.longitude, user.latitude)) < 10:
            yield tobject

keepeds = []

for i, tobject in enumerate(gen_wanteds()):
    keepeds.append(tobject)
    # make a blank image for the text, initialized
    # to transparent text color
    # width, height
    txt = Image.new('RGBA', (900, 300), (255,255,255,255))

    # get a font
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 15)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
#        d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
    # draw text, full opacity
    try:
        d.text((10,40), tobject['object_name'], font=fnt, fill=(0,0,0,255))
    except:
        pass
    try:
        d.text((10,60), tobject['city'], font=fnt, fill=(0,0,0,255))
    except:
        pass
    try:
        d.text((10,80), tobject['url'], font=fnt, fill=(0,0,0,255))
    except:
        pass
    try:
        d.text((10,100), pretiffy(tobject['description']), font=fnt, fill=(0,0,0,255))
    except:
        pass

    txt.save('/var/www/html/24h/tmp/result_' + str(i) + ".png", format="png")


make_map.make_map(keepeds)
