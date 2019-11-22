import pprint

from src.dev_creds import DEV_ID, AUTH_KEY
from src.paladins_api.player_api import PlayerApi

api = PlayerApi(DEV_ID, AUTH_KEY)
# api.get_player('StanisBarathrum', True)
# api.get_player_id_by_name('StanisBarathrum', True)
#


data = api.get_math_history('5225410')
pprint.pprint(data)

# 'Match': 903465556,
# 'Match_Queue_Id': 424,