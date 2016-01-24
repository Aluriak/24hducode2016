"""
Definition of the TObject class

"""



class TObject:
    """Wrapping dictionnary, generating data only if necessary"""

    sources = []

    def __init__(self, data_dict):
        self.data = data_dict

    def __getitem__(self, key):
        if key not in self.data:
            for source in TObject.sources:
                if key in source.keywords():
                    source.enrichment(self.data)
                if key in self.data:
                    break
        return self.data[key]

    def __contains__(self, item):
        return item in self.data

    def __str__(self):
        return str(self.data)
