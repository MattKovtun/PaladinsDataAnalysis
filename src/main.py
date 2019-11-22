from src.dev_creds import DEV_ID, AUTH_KEY

from src.paladins_api.player_api import PlayerApi

api = PlayerApi(DEV_ID, AUTH_KEY).create_session()
api.get_player('StanisBarathrum', True)
api.get_player_id_by_name('StanisBarathrum', True)