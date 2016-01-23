"""
Source object definition.

This is a base class for all sources objects.

"""


class Source:
    """Base class for any source object.
    Add data to dictionnary of data through enrichment method, by adding keys
    and associated values in given dictionnary.

    """

    def enrichment(self, dict_data):
        """Add data to given dictionnary.
        Only keys returned by the keywords static method are added to the dict.

        """
        assert isinstance(dict_data, dict)  # keep this line in subclasses
        return dict_data  # No modification by default

    @staticmethod
    def keywords():
        """Return a set of string, that are all possible keys addable by
        enrichment method

        """
        return set()
