import dash_core_components as dcc


def range_slider(df, tiers):
    uniq = df['tier'].unique()
    mn = min(uniq)
    mx = max(uniq)
    return dcc.RangeSlider(
        id='tier-slider',
        min=mn,
        max=mx,
        marks={int(i): {'label': tiers[i], 'style': {'color': 'grey'}} for i in uniq},
        value=[mn, mx],
        updatemode='drag')
