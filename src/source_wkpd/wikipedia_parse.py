"""
Wikipédia interrogation

"""

# Custom imports
import wikipedia
import requests
from src.default import *

# Config
wikipedia.set_lang("fr")


def get_wikipedia_data(thing):
    """Get info about the given thing on wikipedia

    """

    article_titles = wikipedia.search(thing)
#    Do a Wikipedia search for query.
#
#    Keyword arguments:
#
#        results - the maxmimum number of results returned
#        suggestion - if True, return results and suggestion (if any) in a tuple

    return [get_wikipedia_article_info(article_title) for article_title 
                in article_titles]


def get_wikipedia_data_near_coords(latitude, longitude):
    """Get 10 data max near (10km) gps coords

    ex :GmapLatitude":"47.9908779", "GmapLongitude":"0.24142796"

    :param arg1: latitude
    :param arg2: longitude
    :type arg1: <float>
    :type arg2: <float>

    """

    # Get titles of pages
    #wikipedia.geosearch(latitude, longitude, results=10, radius=10000)
    #    Keyword arguments:
    #
    #        title - The title of an article to search for
    #        results - the maximum number of results returned
    #        radius - Search radius in meters. The value must be between 10 and 10000
    article_titles = wikipedia.geosearch(float(latitude), float(longitude))

    return [get_wikipedia_article_info(article_title) for article_title 
                in article_titles]


def get_wikipedia_article_info(article_title, sentences=4):
    """Return informations about an article, according to the given title.

    :param arg1: Title of the article.
    :param arg2: Number of sentences for the summary (default: 4).
    :type arg1: <str>
    :type arg2: <int>
    :return: dict of new elements with keys : 
        FIELD_NAME, FIELD_COORDINATES, FIELD_DESCRIPTION, URL
    :rtype: <dict>

    """

    def round_this_now(tpl):
        """Round values"""
        try:
            return (round(float(tpl[0]), 6), round(float(tpl[1]), 6))
        except:
            return ('','')

    # Get article page
    page = wikipedia.WikipediaPage(title=article_title, pageid=None)
    # categories
    #    List of categories of a page.
    #content
    #    Plain text content of the page, excluding images, tables, and other data.
    #coordinates
    #    Tuple of Decimals in the form of (lat, lon) or None
    #html()
    #    Get full page HTML.
    #    Warning
    #    This can get pretty slow on long pages.
    #images
    #    List of URLs of images on the page.
    #links
    #    List of titles of Wikipedia page links on a page.
    #references
    #    List of URLs of external links on a page. May include external links within page that aren’t technically cited anywhere.

    article_attributes = dict()
    try:
        article_attributes[FIELD_COORDINATES]  = round_this_now(page.coordinates)
    except:
        pass
    article_attributes[FIELD_DESCRIPTION] = wikipedia.summary(article_title,
                                                          sentences=sentences)
    article_attributes[FIELD_URL] = get_wikipedia_url_with_pageid(page.pageid)
    article_attributes[FIELD_NAME] = article_title

#    print("coords:", page.coordinates)
#    print("description:", wikipedia.summary(article_title))
#    print("pageid:", page.pageid)
#    print("url:", get_wikipedia_url_with_pageid(page.pageid))

    print(article_attributes)

    return article_attributes


def get_wikipedia_url_with_pageid(pageid):
    """Return url of wikipedia page according to the given pageid.

    :param: pageid from wikipedia API
    :type: <str>
    :return: Return FIELD_URL or ""
    :rtype: <str>
    """

    URL = "https://fr.wikipedia.org/w/api.php?action=query&prop=info&pageids={}&inprop=url&format=json"

    try:
        return requests.get(
            URL.format(pageid)
        ).json()["query"]["pages"][str(pageid)]["canonicalurl"]
    except:
        print("NO URL !")
        return ""


if __name__ == "__main__":

    get_wikipedia_data("abbaye épau")
#    get_wikipedia_data_near_coords(47.9908779, 0.24142796)


