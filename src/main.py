import sys, os

sys.path.insert(0, os.path.abspath('..'))

import pprint, random, json

from src.dev_creds import DEV_ID, AUTH_KEY
from src.paladins_api.player_api import PlayerApi
from src.paladins_api.match_api import MatchApi
from src.constants import SIEGE, TIER_N, DATA_DAILY, RANKED_SIEGE
from src.paladins_api.match import Match
from src.utils import time_stamp, write_all_matches_ids

api = MatchApi(DEV_ID, AUTH_KEY)
today = '20191121'
# data = api.get_match_ids_by_queue(RANKED_SIEGE, today, hour='-1', verbose=False)
# #
pp = './data/daily/ranked_siege/' + today

tier_path = './data/tiers/'

match_ids = []
with open(pp) as input_file:
    input_file.readline()
    for line in input_file:
        line = line.strip()
        match_ids.append(line)

some_matches = random.choices(match_ids, k=50)
print(some_matches)


for match_id in some_matches:
    print(match_id)
    match_details = api.get_match_details(match_id)
    match = Match(match_details)
    tier = max(match.get_league_tiers())

    pp = tier_path + str(tier) + '/' + match_id + '.json'
    with open(pp, 'w') as f:
        json.dump(match_details, f)
