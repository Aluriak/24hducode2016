"""
This modules parses the 'OuvertureGranule' time table into an object
Returns a list of time periods containing the opening times for each day of
the week. Time periods are custom objects.
"""

import datetime
import re

# Regex describing one time period (start || end || days information)
r = re.compile(r'(\d\d/\d\d/\d\d\d\d)\|\|(\d\d/\d\d/\d\d\d\d)\|\|\|\|\|\|(.+)')


class timePeriod():
    """
    Class storing a time period.
    Attributes : look below it's easy
    """

    def __init__(self, period, times):

        self.start = datetime.datetime.strptime(period[0],
                                                '%d/%m/%Y').date()
        self.end = datetime.datetime.strptime(period[1],
                                              '%d/%m/%Y').date()
        self.monday = (times[0], times[1],
                       times[2], times[3])
        self.tuesday = (times[4], times[5],
                        times[6], times[7])
        self.wednesday = (times[8], times[9],
                          times[10], times[11])
        self.thursday = (times[12], times[13],
                         times[14], times[15])
        self.friday = (times[16], times[17],
                       times[18], times[19])
        self.saturday = (times[20], times[21],
                         times[22], times[23])
        self.sunday = (times[24], times[25],
                       times[26], times[27])


def _raw_time_table_parser(timeTable):
    """Get a formatted string, outputs a complex object"""
    timePeriods = []
    openingTimes = []
    # Separates time periods
    splitPeriods = (x for x in timeTable.split('##'))
    # Parse each time period
    for period in splitPeriods:
        temp = re.search(r, period)  # Regex see top of file
        timePeriods.append((temp.group(1), temp.group(2)))
        # Days separated by ||
        openingTimes.append(temp.group(3).split('||'))
    return (timePeriods, openingTimes)


def parsed_time_table(rawTimeTable):
    parsedTimeTable = _raw_time_table_parser(rawTimeTable)
    return tuple(timePeriod(period=period, times=times)
                 for period, times
                 in zip(parsedTimeTable[0], parsedTimeTable[1]))
