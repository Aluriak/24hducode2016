"""
Get text to put in little bubbles from the TObject container
"""

from src import default


def prettify(string, wordsize=10):
    return ' '.join(
        ('\n'+word) if idx % wordsize == 0 else word
        for idx, word in enumerate(string.split())
    )


def generate_lists_for_map(objectsList):
    latitudes = []
    longitudes = []
    text = []
    for tobject in objectsList:
        latitudes.append(tobject[default.FIELD_LATITUDE])
        longitudes.append(tobject[default.FIELD_LONGITUDE])
        text.append(tobject[default.FIELD_NAME] + '\n' +
                    prettify(tobject[default.FIELD_DESCRIPTION]))
    return [latitudes, longitudes, text]
