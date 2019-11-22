# might need to move it to a separate folder
# probably create url builder
import requests

from src.dev_creds import DEV_ID
from src.constants import PALADINS_URL, JSON
from src.utils import make_signature, time_stamp


def create_session(verbose=False):
    endpoint = 'createsession'
    session_url = PALADINS_URL + '/' \
                  + endpoint + JSON + '/' \
                  + DEV_ID + '/' \
                  + make_signature(endpoint) + '/' \
                  + time_stamp()

    r = requests.get(session_url).json()

    if verbose:
        print(r)

    return r['session_id']


def get_player(session_id, player, verbose=False):
    endpoint = 'getplayer'
    url = PALADINS_URL + '/' + endpoint + JSON + '/' + DEV_ID + '/' + make_signature(
        endpoint) + '/' + session_id + '/' + time_stamp() + '/' + player
    r = requests.get(url).json()

    if verbose:
        print(r)

    return r


def get_player_id_by_name(session_id, player_name, verbose=False):
    endpoint = 'getplayeridbyname'
    url = PALADINS_URL + '/' + endpoint + JSON + '/' + DEV_ID + '/' + make_signature(
        endpoint) + '/' + session_id + '/' + time_stamp() + '/' + player_name

    r = requests.get(url).json()

    if verbose:
        print(r)

    return r


if __name__ == "__main__":
    session_id = create_session()

    player = 'StanisBarathrum'
    # player = 'Schmuzzi'
    player = 'AttackOnAttack'

    data = get_player(session_id, player, True)
    # player_id = get_player_id_by_name(session_id, player, True)
    print(data)
