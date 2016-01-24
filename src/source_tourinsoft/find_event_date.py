from request_data import request
from src import default


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


test = findEventDate('FMA072878000016')
print(test)
