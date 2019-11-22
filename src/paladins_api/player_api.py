import requests

from src.paladins_api.basic_api import BasicApi
from src.utils import time_stamp
from src.constants import JSON


class PlayerApi(BasicApi):
    def __init__(self, dev_id, auth_key):
        super().__init__(dev_id, auth_key)

    def get_player(self, player, verbose=False):
        endpoint = 'getplayer'
        url = self._url_builder(player, endpoint)
        r = requests.get(url).json()

        if verbose:
            print(r)

        return r

    def _url_builder(self, endpoint, player):
        return self.paladins_url + '/' \
               + endpoint + JSON + '/' \
               + self.dev_id + '/' \
               + self.make_signature(endpoint) + '/' \
               + self.session_id + '/' \
               + time_stamp() + '/' \
               + player


if __name__ == "__main__":
    from src.dev_creds import AUTH_KEY, DEV_ID

    api = PlayerApi(DEV_ID, AUTH_KEY).create_session()
    api.get_player('StanisBarathrum', True)
