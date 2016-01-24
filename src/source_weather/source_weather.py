"""
Definition of a source than add dumb data

"""
from src.source import Source
from src import default
from . import weather

class SourceWeather(Source):
    """
    Throught Open Weather Map generates today weather and
    expected weather for next days, if possible

    """

    def enrichment(self, data_dict):
        if default.FIELD_LATITUDE in data_dict:
            lat = data_dict[default.FIELD_LATITUDE]
            lon = data_dict[default.FIELD_LONGITUDE]
            data_dict[default.FIELD_WEATHER] = weather.actual(lat, lon)
        if default.FIELD_DATE in data_dict:
            date = data_dict[default.FIELD_DATE]
            if weather.is_predictable(date):
                data_dict[default.FIELD_WEATHER_PREDICTED] = weather.predicted(lat, lon)[str(default.FIELD_DATE)]

        return data_dict

    def keywords(self):
        return {default.FIELD_WEATHER_PREDICTED,
                default.FIELD_WEATHER}
