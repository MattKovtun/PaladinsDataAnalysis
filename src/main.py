import json

from etl.data_transformation import read_tier, form_csv, get_match_info
from etl.match_scrapper import matches_to_tiers, scrap_ranked_matches

from paladins_api.basic_api import BasicApi
from paladins_api.champion_api import ChampionApi
from dev_creds import DEV_ID, AUTH_KEY

api = ChampionApi(DEV_ID, AUTH_KEY)

champions = api.get_champions(verbose=True)

for champ in champions:
    name = champ['Name']
    with open('../data/champions/' + name + '.json', 'w') as f:
        json.dump(champ, f)
