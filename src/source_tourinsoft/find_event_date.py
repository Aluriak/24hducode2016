"""
Find dates associated with an event
Input eventID
Output tuple (Datedebut, Datefin) converted in the right format
"""

from request_data import request


def findEventDate(eventID):
    searchResults = request(collection='OuvertureGranule',
                            filters={'SyndicObjectId': eventID})
    return ((default.date_type_wrapped(
                event['Datedebut'],
                default.TOURINFO_DATE_FORMAT
             ),
             default.date_type_wrapped(
                event['Datefin'],
                default.TOURINFO_DATE_FORMAT
             ))
            for event in searchResults)
