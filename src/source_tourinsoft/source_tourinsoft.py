"""
Definition of source Tourinsoft
Gets data from the two databases Events and Places using tourinsoft's API
Inherits from the SOURCE global class

"""
# from src.source import Source
from .request_data import request


class SourceTourinsoft(Source):

    def spawn_all(self):
        return request()

    def keywords(self):
        return {self.key}
