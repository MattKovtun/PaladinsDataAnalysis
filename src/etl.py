import os, json
import pandas as pd
import random

from dev_creds import DEV_ID, AUTH_KEY
from paladins_api.match_api import MatchApi
from constants import RANKED_SIEGE
from constants import TIER_N
from paladins_api.match import Match
from paladins_api.match_player import MatchPlayer

tiers_path = '../data/tiers/'


def scrap_ranked_matches(date):
    api = MatchApi(DEV_ID, AUTH_KEY)
    data = api.get_match_ids_by_queue(RANKED_SIEGE, date, hour='-1', verbose=False)
    pp = '../data/daily/ranked_siege/' + date

    with open(pp, 'w') as f:
        f.write(str(len(data)) + '\n')
        for line in data:
            f.write(line['Match'] + '\n')


def matches_to_tiers(date, n_matches=20):
    matches_id_path = '../data/daily/ranked_siege/' + date

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
        tier = max(match.get_league_tiers)

        pp = tiers_path + str(tier) + '/' + match_id + '.json'
        with open(pp, 'w') as f:
            json.dump(match_details, f)


def form_ban_summary_csv(name):
    def get_match_info(match_path):
        with open(match_path) as f:
            match_info = json.loads(f.read())

        df = pd.DataFrame()
        match = Match(match_info)

        bans = match.get_bans
        time = match.get_time
        tier = max(match.get_league_tiers)

        if None in bans: return df

        df['time'] = [time] * len(bans)
        df['tier'] = [tier] * len(bans)
        df['ban'] = bans
        return df

    def read_tier(path, tier):
        path = path + '/' + tier
        matches = os.listdir(path)
        df = pd.DataFrame()

        for match in matches:
            ddf = get_match_info(path + '/' + match)
            df = df.append(ddf)
        return df

    processed_file = '../data/processed/ban_summary/' + name
    df = pd.DataFrame()

    for i in range(TIER_N):
        tier = str(i)
        ddf = read_tier(tiers_path, tier)
        df = df.append(ddf)

    df.to_csv(processed_file, index=False)


def form_match_summary(name):
    tiers = os.listdir(tiers_path)
    data = []
    for tier in tiers:
        tpath = tiers_path + tier + '/'
        matches = os.listdir(tpath)
        for match in matches:
            with open(tpath + '/' + match) as f:
                d = json.load(f)
            for player in d:
                m = MatchPlayer(player)
                data.append([m.match_id,
                             m.hero,
                             m.winner,
                             m.healing,
                             m.damage_taken,
                             m.damage_done,
                             m.tier,
                             m.time])

    df = pd.DataFrame(data,
                      columns=['matchid', 'hero', 'winner', 'healing', 'damage_taken', 'damage_done', 'tier', 'time'])
    processed_file = '../data/processed/match_summary/' + name
    df.to_csv(processed_file, index=False)


if __name__ == "__main__":
    date = '20191208'
    scrap_ranked_matches(date)
    matches_to_tiers(date, 2000)
    form_ban_summary_csv('v4.csv')
    form_match_summary('v4.csv')
