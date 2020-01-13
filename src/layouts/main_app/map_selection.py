import dash_core_components as dcc


def map_selection(maps):
    options = [{'label': m[7:], 'value': m} for m in maps]
    return dcc.Dropdown(id='maps-dropdown',
                        options=options,
                        value=maps,
                        multi=True,
                        style={'width': '650px'})
