from paladins_api.constants import JSON
from paladins_api.utils import time_stamp
from paladins_api.basic_api import BasicApi


class MatchApi(BasicApi):
    def __init__(self, dev_id, auth_key):
        super().__init__(dev_id, auth_key)

    def get_top_matches(self, verbose=False):
        # Response 200, empty array
        endpoint = 'gettopmatches'
        url = self._url_builder(endpoint)
        return self._send_request(url, verbose)

    def get_motd(self, verbose=False):
        endpoint = 'getmotd'
        url = self._url_builder(endpoint)
        return self._send_request(url, verbose)

    def get_match_details(self, match_id, verbose=False):
        endpoint = 'getmatchdetails'
        url = self._url_builder(endpoint, match_id)
        return self._send_request(url, verbose)

    def get_match_ids_by_queue(self, queue, date, hour, mm='', verbose=False):
        # Only valid values for mm are “00”, “10”, “20”, “30”, “40”, “50”
        endpoint = 'getmatchidsbyqueue'
        url = self._url_builder(endpoint, queue)
        url = url + '/' + date + '/' + hour
        if mm:
            url += ',' + mm
        return self._send_request(url, verbose)

    def _url_builder(self, endpoint, match_id=''):
        url = self.paladins_url + '/' \
              + endpoint + JSON + '/' \
              + self.dev_id + '/' \
              + self.make_signature(endpoint) + '/' \
              + self.session_id + '/' \
              + str(time_stamp())
        if match_id:
            url += '/' + match_id

        return url
