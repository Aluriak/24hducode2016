import datetime
import re

r = re.compile(r'(\d\d/\d\d/\d\d\d\d)\|\|(\d\d/\d\d/\d\d\d\d)\|\|\|\|\|\|(.+)')


class timePeriod():

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


class TimeTableParser():

    @staticmethod
    def parseRawTimeTable(timeTable):
        timePeriods = []
        openingTimes = []
        splitPeriods = (x for x in timeTable.split('##'))
        for period in splitPeriods:
            temp = re.search(r, period)
            timePeriods.append((temp.group(1), temp.group(2)))
            openingTimes.append(temp.group(3).split('||'))

        return([timePeriods, openingTimes])

    def __init__(self, rawTimeTable):
        parsedTimeTable = TimeTableParser.parseRawTimeTable(rawTimeTable)
        self.timePeriods = [timePeriod(period=period, times=times)
                            for period, times
                            in zip(parsedTimeTable[0], parsedTimeTable[1])]
