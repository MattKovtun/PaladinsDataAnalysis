from paladins_api.basic_api import BasicApi
from paladins_api.utils import time_stamp
from paladins_api.constants import JSON


class PlayerApi(BasicApi):
    def __init__(self, dev_id, auth_key):
        super().__init__(dev_id, auth_key)

    def get_player(self, player, verbose=False):
        endpoint = 'getplayer'
        url = self._url_builder(endpoint, player)
        return self._send_request(url, verbose)

    def get_player_id_by_name(self, player, verbose=False):
        endpoint = 'getplayeridbyname'
        url = self._url_builder(endpoint, player)
        return self._send_request(url, verbose)

    def get_math_history(self, player_id, verbose=False):
        endpoint = 'getmatchhistory'
        url = self._url_builder(endpoint, player_id)
        return self._send_request(url, verbose)

    def get_queue_stats(self, player_id, queue, verbose=False):
        endpoint = 'getqueuestats'
        url = self._url_builder(endpoint, player_id, queue)
        return self._send_request(url, verbose)

    def _url_builder(self, endpoint, player, queue=''):
        base_url = self.paladins_url + '/' \
                   + endpoint + JSON + '/' \
                   + self.dev_id + '/' \
                   + self.make_signature(endpoint) + '/' \
                   + self.session_id + '/' \
                   + str(time_stamp()) + '/' \
                   + player
        if queue:
            base_url += '/' + queue
        return base_url




