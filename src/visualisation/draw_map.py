# -*- coding: utf-8 -*-

##########
# IMPORT #
##########
import plotly.offline as py
import plotly.tools as tls


tls.set_credentials_file(username='ducktypers', api_key='fd81wnx3lh')

########
# MAIN #
########


def draw_map(lon, lat, text, titre='NO TITLE'):
    """
    Take 3 list as input, and the title of the map.
    """

    py.plot({                      # use `py.iplot` inside the ipython notebook
        "data": [{
        'type': 'scattergeo',
        'locationmode': 'france',
        'lon': lon,
        'lat': lat,
        'text': text,
        'mode': 'markers',
        'marker': dict(
            size = 8,
            opacity = 0.8,
            line = dict(width=1, color="rgb(102,102,102)")
        )
    }],
    "layout": {
        'title': str(titre),
        'geo': dict(scope='europe',
                    projection=dict( type='albers europe' ),
                    showland = True,
                    landcolor = "rgb(200, 200, 200)",
                subunitcolor = "rgb(217, 217, 217)",
                countrycolor = "rgb(217, 217, 217)",
                countrywidth = 1,
                subunitwidth = 1)
    }
    }, filename='interactive_map',      # name of the file as saved in your plotly account
   #sharing='public'
   )
