import requests
import hashlib

from paladins_api.utils import time_stamp
from paladins_api.constants import JSON, PALADINS_URL


class BasicApi:
    def __init__(self, dev_id, auth_key):
        self.dev_id = dev_id
        self.auth_key = auth_key
        self.paladins_url = PALADINS_URL
        self.session_id = self.create_session()

    def create_session(self, verbose=False):
        endpoint = 'createsession'
        session_url = self.paladins_url + '/' \
                      + endpoint + JSON + '/' \
                      + self.dev_id + '/' \
                      + self.make_signature(endpoint) + '/' \
                      + str(time_stamp())

        r = self._send_request(session_url, verbose)
        return r['session_id']

    def make_signature(self, endpoint):
        sig = self.dev_id + endpoint + self.auth_key + str(time_stamp())
        return hashlib.md5(sig.encode('utf-8')).hexdigest()

    def get_data_used(self, verbose=False):
        endpoint = 'getdataused'
        url = self.paladins_url + '/' \
              + endpoint + JSON + '/' \
              + self.dev_id + '/' \
              + self.make_signature(endpoint) + '/' \
              + self.session_id + '/' \
              + str(time_stamp())

        return self._send_request(url, verbose)

    def _send_request(self, url, verbose=False):
        if verbose:
            print("URL:", url)

        r = requests.get(url)
        if verbose:
            print("Response:", r)

        r = r.json()
        if verbose:
            print("json:", r)
        return r

    def _url_builder(self, endpoint):
        pass
