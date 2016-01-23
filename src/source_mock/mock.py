"""
Definition of a source than add dumb data

"""
from src.source import Source

class SourceMock(Source):
    """Add a funny key with a funny value in the given dict"""

    def __init__(self, funny_message="Java.OutOfMemoryError"
                 funny_key="Who's there ?"):
        self.funny_message = funny_message
        self.funny_key     = funny_key

    def enrichment(self, data_dict)
        data_dict[self.funny_key] = self.funny_message
        return data_dict

    def keywords(self):
        return {self.funny_key}
