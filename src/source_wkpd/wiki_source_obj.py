"""
Definition of a source than adds Wikipédia data.
"""

from src.default import *
from src.source import Source
#import src.wkpd.wikipedia_parse as wkp
from src.source_wkpd import wikipedia_parse as wkp

class WikiSource(Source):
    """docstring de class"""
    
    def __init__(self):
        self.funny_keys = set()

    def enrichment(self, data_dict):
        
        # Initialize linked_elems
        # data_dict['linked_elems'] = list()
        
        # Update data according to GPS coords
#        if FIELD_LATITUDE in data_dict:
#
#            print("Processing: Coordinates")
#            data_dict['linked_elems'] += wkp.get_wikipedia_data_near_coords(
#                                            data_dict[FIELD_LATITUDE],
#                                            data_dict[FIELD_LONGITUDE]
#                                         )
#            print(data_dict['linked_elems'])
#
#            [self.funny_keys.update(elem.keys()) for elem 
#                in data_dict['linked_elems']]

        # Update data according to a SyndicObjectName
        if FIELD_NAME in data_dict:
            
            # print("Processing:", FIELD_NAME)
            try:
                payload = wkp.get_wikipedia_data(data_dict[FIELD_NAME])[0]
                data_dict[FIELD_DESCRIPTION] = payload[FIELD_DESCRIPTION]
                data_dict[FIELD_URL] = payload[FIELD_URL]
            except IndexError:
                data_dict[FIELD_DESCRIPTION] = None
                data_dict[FIELD_URL] = None
            # print('PAYLOAD:', payload.__class__, payload)

            # [self.funny_keys.update(elem.keys()) for elem 
                # in data_dict['linked_elems']]
        
        # print("RETURNED KEYS", self.funny_keys)
        
        return data_dict

    def keywords(self):
        return {FIELD_URL, FIELD_DESCRIPTION}

if __name__ == "__main__":
    
    obj = dict()
    obj[FIELD_COORDINATES] = (48.515079, 4.298639)
    obj[FIELD_NAME] = "Europajazz"
    
    wk_src = WikiSource()
    
    print(wk_src.enrichment(obj))
