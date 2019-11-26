import sys, os

sys.path.insert(0, os.path.abspath('../'))

import random, json
from datetime import timedelta, datetime

from src.dev_creds import DEV_ID, AUTH_KEY
from src.paladins_api.match_api import MatchApi
from src.constants import SIEGE, TIER_N, DATA_DAILY, RANKED_SIEGE
from src.paladins_api.match import Match


def scrap_ranked_matches():
    api = MatchApi(DEV_ID, AUTH_KEY)
    today = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
    data = api.get_match_ids_by_queue(RANKED_SIEGE, today, hour='-1', verbose=False)
    pp = '../data/daily/ranked_siege/' + today

    with open(pp, 'w') as f:
        f.write(str(len(data)) + '\n')
        for line in data:
            f.write(line['Match'] + '\n')


def match_to_tier(match_path, n_matches=20):
    tier_path = '../data/tiers/'

    match_ids = []
    with open(match_path) as input_file:
        input_file.readline()
        for line in input_file:
            line = line.strip()
            match_ids.append(line)

    some_matches = random.choices(match_ids, k=n_matches)

    api = MatchApi(DEV_ID, AUTH_KEY)
    print(some_matches)
    for match_id in some_matches:
        print(match_id)
        match_details = api.get_match_details(match_id)
        match = Match(match_details)
        tier = max(match.get_league_tiers())

        pp = tier_path + str(tier) + '/' + match_id + '.json'
        with open(pp, 'w') as f:
            json.dump(match_details, f)


if __name__ == "__main__":
    match_path = '../data/daily/ranked_siege/20191124'
    match_to_tier(match_path, 10)
    # scrap_ranked_matches()
