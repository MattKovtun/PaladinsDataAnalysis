
import random, json
from datetime import timedelta, datetime

from dev_creds import DEV_ID, AUTH_KEY
from paladins_api.match_api import MatchApi
from constants import RANKED_SIEGE
from paladins_api.match import Match


def scrap_ranked_matches(date):
    api = MatchApi(DEV_ID, AUTH_KEY)
    data = api.get_match_ids_by_queue(RANKED_SIEGE, date, hour='-1', verbose=False)
    pp = '../data/daily/ranked_siege/' + date

    with open(pp, 'w') as f:
        f.write(str(len(data)) + '\n')
        for line in data:
            f.write(line['Match'] + '\n')


def matches_to_tiers(matches_id, n_matches=20):
    matches_id_path = '../data/daily/ranked_siege/' + matches_id
    tier_path = '../data/tiers/'

    match_ids = []
    with open(matches_id_path) as input_file:
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
    date = '20191130'
    # scrap_ranked_matches(date)

    matches_to_tiers(date, 200)
