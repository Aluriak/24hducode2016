"""
TObject stores an object obtained through the tounrinsoft API
This object can be an event or a place
For now, it only contains a dictionary with values for each property
obtained from the json dictionary output of a request on this API
"""


class TObject:

    FILTERED_OUT = set()  # Some keys are useless for us, we filter them out

    def __init__(self, data):
        self.values = data
        assert data.__class__ is dict  # JSON output is a dict

    @staticmethod
    def filter_input(jsondict):
        """
        Input: request's JSON dictionary output
        Output: a dictionary with unwanted values and None values filtered out
        """
        return {
            key: value
            for key, value in jsondict.items()
            if key not in TObject.FILTERED_OUT and value is not None
        }

    @staticmethod
    def create_from_dict(dictionary):
        """
        Creator for TObject from a request's JSON dictionary output
        """
        return TObject(TObject.filter_input(dictionary))

# Usage example
# test = TObject.create_from_dict({"test": 'lala', "test2": 5})
