import pandas as pd


def prepare_data(filename):
    df = pd.read_csv(filename)
    df['time'] = pd.to_datetime(df['time'])
    df['date'] = df['time'].dt.date
    x = df['ban'].unique()
    x.sort()
    y = [0] * len(x)
    data = dict(zip(x, y))
    return df, data
