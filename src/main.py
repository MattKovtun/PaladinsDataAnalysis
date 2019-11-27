import os, json
import pandas as pd

from constants import TIER_N

from paladins_api.match import Match


def read_tier(path, tier):
    path = path + '/' + tier
    matches = os.listdir(path)
    df = pd.DataFrame()

    for match in matches:
        ddf = get_match_info(path + '/' + match)
        df = df.append(ddf)
    return df


def get_match_info(match_path):
    with open(match_path) as f:
        match_info = json.loads(f.read())

    df = pd.DataFrame()
    match = Match(match_info)

    bans = match.get_bans()
    time = match.get_time()
    tier = max(match.get_league_tiers())

    if None in bans: return df

    df['time'] = [time] * len(bans)
    df['tier'] = [tier] * len(bans)
    df['ban'] = bans
    return df


def main():
    processed_file = '../data/processed/v1.csv'
    tiers_path = '../data/tiers'
    df = pd.DataFrame()

    for i in range(TIER_N):
        tier = str(i)
        ddf = read_tier(tiers_path, tier)
        df = df.append(ddf)

    df.to_csv(processed_file, index=False)


if __name__ == "__main__":
    main()
