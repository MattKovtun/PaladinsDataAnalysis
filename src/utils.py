import pandas as pd


def prepare_data(filename):
    df = pd.read_csv(filename)
    df['time'] = pd.to_datetime(df['time'], format='%m/%d/%Y %I:%M:%S %p')  # speeds up like 10 times
    df['date'] = df['time'].dt.date
    return df


def create_hero_list(df):
    x = df['ban'].unique()
    x.sort()
    y = [0] * len(x)
    return dict(zip(x, y))


def calc_ban_rate(df):
    field = 'ban'
    matches = df['matchid'].nunique()
    heroes = df[field].unique()
    heroes.sort()
    ban_rate = []
    for h in heroes:
        ban_rate.append((h, df[df[field] == h].shape[0] / matches))
    return ban_rate


def calc_pick_rate(bans, picks):
    p_field = 'hero'
    b_field = 'ban'

    total_matches = bans['matchid'].nunique()
    heroes = bans[p_field].unique()
    heroes.sort()
    pick_rate = []
    for h in heroes:
        bans_n = picks[picks[b_field] == h].shape[0]
        matches = total_matches - bans_n

        pick_rate.append(
            (h, bans[bans[p_field] == h].shape[0] / matches)
        )

    return pick_rate
