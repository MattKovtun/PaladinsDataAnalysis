from src.constants import JSON
from src.utils import time_stamp
from src.paladins_api.basic_api import BasicApi


class MatchApi(BasicApi):
    def __init__(self, dev_id, auth_key):
        super().__init__(dev_id, auth_key)

    def get_top_matches(self, verbose=False):
        endpoint = 'gettopmatches'
        url = self._url_builder(endpoint)
        return self._send_request(url, verbose)

    def get_motd(self, verbose=False):
        endpoint = 'getmotd'
        url = self._url_builder(endpoint)
        return self._send_request(url, verbose)

    def _url_builder(self, endpoint, match_id=''):
        url = self.paladins_url + '/' \
              + endpoint + JSON + '/' \
              + self.dev_id + '/' \
              + self.make_signature(endpoint) + '/' \
              + self.session_id + '/' \
              + time_stamp()
        if match_id:
            url += '/' + match_id

        return url


if __name__ == "__main__":
    from src.dev_creds import DEV_ID, AUTH_KEY

    api = MatchApi(DEV_ID, AUTH_KEY)
    api.get_motd(True)
