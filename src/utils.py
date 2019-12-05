import pandas as pd


def prepare_data(filename):
    df = pd.read_csv(filename)
    df['time'] = pd.to_datetime(df['time'])
    df['date'] = df['time'].dt.date
    return df


def create_hero_list(df):
    x = df['ban'].unique()
    x.sort()
    y = [0] * len(x)
    return dict(zip(x, y))
