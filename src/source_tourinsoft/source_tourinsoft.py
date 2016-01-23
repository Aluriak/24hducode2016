"""
Definition of source Tourinsoft
Gets data from the two databases Events and Places using tourinsoft's API
Inherits from the SOURCE global class

"""
# from src.source import Source


class SourceTourinsoft():

    def enrichment(self, data_dict):
        data_dict[self.key] = self.value
        return data_dict

    def keywords(self):
        return {self.key}
