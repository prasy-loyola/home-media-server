# VERSION: 0.1
# AUTHORS: prasyloyola
# CONTRIBUTORS: Prasanna Selvaraj (prasy.loyola@gmail.com)

from novaprinter import prettyPrinter
from helpers import retrieve_url, json


class tamilblasters(object):
    name = "Tamil Blasters"
    url = 'https://tamilblasters.re/'
    supported_categories = {'all': '0', 'movies': '6', 'tv': '4', 'music': '1'}
    search_url = "https://tamilblasters.sepra.hopto.org/"

    def search(self, what, cat='all'):
        """ Performs search"""
        query = self.search_url + '/search?queryString=' + what
        results_json = retrieve_url(query)
        response_json = json.loads(results_json)

        # check empty response
        if len(response_json.result) == 0:
            return

        # parse results
        for result in response_json.result:
            res = {
                'link': result['location'],
                'name': result['name'],
                'size': -1,
                'seeds': -1,
                'leech': -1,
                'engine_url': self.url,
                'desc_link': result['location']
            }
            prettyPrinter(res)
