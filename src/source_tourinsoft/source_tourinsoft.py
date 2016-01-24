"""
Definition of source Tourinsoft
Gets data from the two databases Events and Places using tourinsoft's API
Inherits from the SOURCE global class

"""
from src.source import Source
from .request_data import request_events, request_places
from .normalization import normalized_keys


class SourceTourinsoft(Source):

    def spawn_all(self):
        for event in request_events():
            yield normalized_keys(event, isevent=True)
        for place in request_places():
            yield normalized_keys(place, isevent=False)

    def keywords(self):
        return {self.key}
