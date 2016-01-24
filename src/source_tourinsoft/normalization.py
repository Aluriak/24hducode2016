"""
Normalization of the data.

Define mainly a dict {key in turinsoft: (normalized key, type)}.
Define also a method that turn a dict with turinsoft keys into
a dict of normalized keys.

"""
from src import default
from .timetable_parser import parsed_time_table


# Dirty keys: (normalized key, type converter)
KEYS_ASSOCIATION = {
    'SyndicObjectID'   : (default.FIELD_ID, str),
    'SyndicObjectName' : (default.FIELD_NAME, str),
    'ObjectTypeName'   : (default.FIELD_TYPE, str),
    'Updated'          : (default.FIELD_UPDATED, default.date_type),
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
            try:
                # print('INLOOP:', type_conv(data_dict[unkey]))
                norm_data[normkey] = type_conv(value)
                # print(norm_data[normkey])
            except AttributeError:
                pass
    return norm_data
