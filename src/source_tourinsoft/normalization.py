"""
Normalization of the data.

Define mainly a dict {key in turinsoft: (normalized key, type)}.
Define also a method that turn a dict with turinsoft keys into
a dict of normalized keys.

"""
from functools import partial
from datetime import datetime
from src import default
from .timetable_parser import parsed_time_table


# Types definition
TOURINFO_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
def date_type_wrapped(string, format):
    """Wrapper around datetime, allowing usage of keywords arguments"""
    if '.' in string:
        string = string.split('.')[0]
    return datetime.strptime(string, format)
date_type = partial(date_type_wrapped, format=TOURINFO_DATE_FORMAT)


# Dirty keys: (normalized key, type converter)
KEYS_ASSOCIATION = {
    'SyndicObjectID'   : (default.FIELD_ID, str),
    'SyndicObjectName' : (default.FIELD_NAME, str),
    'ObjectTypeName'   : (default.FIELD_TYPE, str),
    'Updated'          : (default.FIELD_UPDATED, date_type),
    'GmapLatitude'     : (default.FIELD_LATITUDE, str),
    'GmapLongitude'    : (default.FIELD_LONGITUDE, str),
    'Commune'          : (default.FIELD_CITY, str),
    'CodePostal'       : (default.FIELD_ZIPCODE, int),
    'OuvertureGranule' : (default.FIELD_OPENING, parsed_time_table),
    'TarifGratuit'     : (default.FIELD_FREE, bool),
}


def normalized_keys(data_dict, isevent):
    """Return a data_dict, equivalent to given one, but with normalized
    keys and values"""
    norm_data = {default.FIELD_EVENT: bool(isevent)}
    for unkey, (normkey, type_conv) in KEYS_ASSOCIATION.items():
        # print('LOOP:', unkey, (normkey, type_conv))
        value = data_dict.get(unkey, None)
        if value:
            # print('INLOOP:', type_conv, data_dict[unkey])
            # print('INLOOP:', type_conv(data_dict[unkey]))
            norm_data[normkey] = type_conv(value)
            print(norm_data[normkey])
    return norm_data
