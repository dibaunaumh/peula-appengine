from google.appengine.api.urlfetch import fetch
from django.utils import simplejson

TWITTER_SEARCH_URL = 'http://search.twitter.com/search.json?q=%s'


def get_mentions(s):
    """
    Get mentions from social media sources, for now only Twitter.
    """
    mentions = []
    url = TWITTER_SEARCH_URL % s
    res = fetch(url)
    json = res.content
    ret = simplejson.loads(json)
    for e in ret["results"]:
        mentions.append((e["from_user"], e["text"], e["profile_image_url"]))
    return mentions
        