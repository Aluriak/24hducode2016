"""
Define the constructor of T-Object.
Return the final set of TObjects, based on given sources and given json

"""
from .source import Source
from .tobject import TObject


class TObjectFactory:
    """Encapsulation of the enrichment on json TObjects, through given sources.

    """

    def __init__(self, sources):
        self.sources = tuple(sources)
        TObject.sources = self.sources
        assert all(isinstance(source, Source) for source in self.sources)

    def tobjects(self, json_data):
        """Return the final set of TObjects, based on given sources and json"""
        for tobject in json_data:
            yield TObject(tobject)
