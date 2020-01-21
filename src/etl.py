import os, json
import pandas as pd
import random

import tqdm
from datetime import timedelta
from dev_creds import DEV_ID, AUTH_KEY
from paladins_api.match_api import MatchApi
from constants import RANKED_SIEGE
from constants import TIER_N
from paladins_api.match import Match
from paladins_api.match_player import MatchPlayer

tiers_path = '../data/tiers/'
ranked_siege = '../data/daily/ranked_siege/'


def scrap_ranked_matches(start_date, end_date):
    def scrap_match(date):
        data = api.get_match_ids_by_queue(RANKED_SIEGE, date, hour='-1', verbose=True)
        pp = ranked_siege + date

        with open(pp, 'w') as f:
            f.write(str(len(data)) + '\n')
            for line in data:
                f.write(line['Match'] + '\n')

    api = MatchApi(DEV_ID, AUTH_KEY)
    end_date = pd.to_datetime(end_date).date()
    date = pd.to_datetime(start_date).date()
    while date != end_date:
        print(date)
        scrap_match(date.strftime('%Y%m%d'))
        date += timedelta(days=1)


def matches_to_tiers(date, n_matches=20):
    matches_id_path = ranked_siege + date

    match_ids = []
    with open(matches_id_path) as input_file:
        input_file.readline()
        for line in input_file:
            line = line.strip()
            match_ids.append(line)

    some_matches = random.choices(match_ids, k=n_matches)

    api = MatchApi(DEV_ID, AUTH_KEY)
    for match_id in tqdm.tqdm(some_matches):
        match_details = api.get_match_details(match_id)
        match = Match(match_details)
        tier = max(match.get_league_tiers)
        if tier == 0: continue

        pp = tiers_path + str(tier) + '/' + match_id + '.json'
        with open(pp, 'w') as f:
            json.dump(match_details, f)


def form_ban_summary_csv(name):
    def get_match_info(match_path):
        with open(match_path) as f:
            if not match_path.endswith('.json'): return []
            match_info = json.loads(f.read())

        match = Match(match_info)

        bans = match.get_bans
        time = match.get_time
        map = match.get_map
        tier = max(match.get_league_tiers)

        match_data = []

        if None in bans: return match_data

        for ban in bans:
            match_data.append([time, tier, map, ban])

        return match_data

    def read_tier(path, tier):
        path = path + tier
        matches = os.listdir(path)
        tier_data = []

        for match in matches:
            d = get_match_info(path + '/' + match)
            tier_data.extend(d)
        return tier_data

    processed_file = '../data/processed/ban_summary/' + name
    data = []

    for i in range(TIER_N):
        tier = str(i)
        data.extend(read_tier(tiers_path, tier))

    df = pd.DataFrame(data, columns=['time', 'tier', 'map', 'ban'])
    df.to_csv(processed_file, index=False)


def form_match_summary(name):
    tiers = os.listdir(tiers_path)
    data = []
    for tier in tiers:
        tpath = tiers_path + tier + '/'
        matches = os.listdir(tpath)
        for match in matches:
            if not (tpath + '/' + match).endswith('.json'): continue
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
                             m.time,
                             m.map])

    df = pd.DataFrame(data,
                      columns=['matchid', 'hero', 'winner', 'healing',
                               'damage_taken', 'damage_done', 'tier',
                               'time', 'map'])
    processed_file = '../data/processed/match_summary/' + name
    df.to_csv(processed_file, index=False)


def total_matches_per_day(start_date, end_date):
    end_date = pd.to_datetime(end_date).date()
    start_date = pd.to_datetime(start_date).date()
    days_data = dict()
    while start_date != end_date:
        days_data[start_date] = 0
        start_date += timedelta(days=1)

    print()
    tiers = os.listdir(tiers_path)
    for tier in tqdm.tqdm(tiers):
        tpath = tiers_path + tier + '/'
        matches = os.listdir(tpath)
        for match in matches:
            with open(tpath + '/' + match) as f:
                match_info = json.loads(f.read())

            match = Match(match_info)
            print(match)
            t = match.get_time
            t = pd.to_datetime(t, format='%m/%d/%Y %I:%M:%S %p').date()

            if t in days_data:
                days_data[t] += 1

    print(days_data)


def clean_new():
    tt = pd.to_datetime('2020', format='%Y').date()
    print(tt)
    tiers = os.listdir(tiers_path)
    for tier in tiers:
        pp = tiers_path + tier
        if os.path.isdir(pp):
            matches = os.listdir(pp)
            for m in matches:
                # os.remove(pp + '/' + m)
                pass


if __name__ == "__main__":
    import time

    date = '20200120'
    end_date = '20200121'
    # # total_matches_per_day(date, end_date)
    # scrap_ranked_matches(date, end_date)

    #
    # datetime.date(2019, 12, 5): 0, datetime.date(2019, 12, 6): 1905, datetime.date(
    #     2019, 12, 7): 1854, datetime.date(2019, 12, 8): 1861}

    # t = time.time()
    # matches_to_tiers(date, 300)
    # t1 = time.time()
    # print(t1 - t)

    form_ban_summary_csv('v6.csv')
    # # t2 = time.time()
    # # print(t2 - t1)
    #
    form_match_summary('v6.csv')
    # t3 = time.time()
    # print(t3 - t2)
# #
