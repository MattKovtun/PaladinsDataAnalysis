from paladins_api.basic_api import BasicApi
from paladins_api.constants import JSON
from paladins_api.utils import time_stamp
from paladins_api.constants import ENGLISH


class ChampionApi(BasicApi):
    def __init__(self, dev_id, auth_key):
        super().__init__(dev_id, auth_key)

    def get_champions(self, language=ENGLISH, verbose=False):
        endpoint = "getchampions"
        url = self._url_builder(endpoint, language)
        return self._send_request(url, verbose)

    def _url_builder(self, endpoint, language):
        base_url = self.paladins_url + '/' \
                   + endpoint + JSON + '/' \
                   + self.dev_id + '/' \
                   + self.make_signature(endpoint) + '/' \
                   + self.session_id + '/' \
                   + str(time_stamp()) + '/' \
                   + language

        return base_url
