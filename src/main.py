import sys, os

sys.path.insert(0, os.path.abspath('..'))

import pprint

from src.dev_creds import DEV_ID, AUTH_KEY
from src.paladins_api.player_api import PlayerApi
from src.paladins_api.match_api import MatchApi
from src.constants import SIEGE

# api = PlayerApi(DEV_ID, AUTH_KEY)
# api.get_player('StanisBarathrum', True)
# api.get_player_id_by_name('StanisBarathrum', True)
#
player_id = '5225410'
#
# data = api.get_math_history(player_id=player_id)
# pprint.pprint(data)
#
#
# match_history = api.get_queue_stats(player_id, SIEGE, True)
# pprint.pprint(match_history)

# 'Match': 903465556,
# 'Match_Queue_Id': 424,


api = MatchApi(DEV_ID, AUTH_KEY)
# data = api.get_match_ids_by_queue(SIEGE, '20191121', '-1', verbose=False)
# pprint.pprint(data)


data = api.get_match_details('905339427')
pprint.pprint(data)