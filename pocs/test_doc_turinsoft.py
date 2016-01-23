"""
Test de la doc turinsoft:
    http://api-doc.tourinsoft.com/#/questionnaire-web

prospose quelques fonctions de wrapping

"""

import requests


URL = 'http://wcf.tourinsoft.com/QuestionnaireWeb/QuestionnaireWebService.svc/{}/{}/{}'
AUTH = ('cdt72', '969e24f9-75a2-4cc6-a46c-db1f6ebbfe97')


def access(service, client, questionnaire, auth=AUTH):
    """Return json object on given data"""
    return requests.get(URL.format(service, client, questionnaire),
                        auth=auth).json()

print(access())  # TODO


