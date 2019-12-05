import json


from paladins_api.basic_api import BasicApi
from paladins_api.champion_api import ChampionApi
from dev_creds import DEV_ID, AUTH_KEY

api = BasicApi(DEV_ID, AUTH_KEY)

print(api.get_data_used(True))
