# bool(v)
from request_data import request
from collections import Counter


def gen_key(property, event=False):
    for tobject in request(event=event):
        for key, value in tobject.items():
            if key.lower().startswith(property):
                yield key


def gen_value(property, event=False):
    property = property.lower()
    for tobject in request(event=event):
        for key, value in tobject.items():
            if key.lower().startswith(property):
                yield value


def gen_value_compare(property1, property2, event=False):
    same, diff = (0, 0)
    for tobject in request(event=event):
        f = 0
        for key, value in tobject.items():
            if key.lower().startswith(property1):
                f += 1
            if key.lower().startswith(property2):
                f += 1
        if f == 2:
            same += 1
        else:
            diff += 1
    return(same, diff)

print(Counter(gen_value("type", event=False)))
# print(gen_value_compare('syndicobjectname', 'nomoffre'))


# class Visite:
#     def __init__(self, sur_demande=False, permanence=False, libre=False,
#                  guidee=False, pedagogique=False, duree_moyenne=0):
#         self._sur_demande, self._permanence = sur_demande, permanence
#         self._guidee, self._libre = guidee, libre
#         self._guidee, self._libre = guidee, libre

#     @property
#     def pedagogique(self):
#         return self._pedagogique


# class VisiteGroupe(Visite):

#     def __init__(self, sur_demande=False, libre=False, pedagogique=False):
#         super().__init__(self, , sur_demande=False, libre=False)


#     @property
#     def sur_demande(self):
#         return False
