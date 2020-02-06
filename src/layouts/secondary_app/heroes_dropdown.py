import dash_core_components as dcc


def heroes_dropdown(heroes):
    options = [{'label': hero, 'value': hero} for hero in heroes]
    return dcc.Dropdown(id='secondary-hero-dropdown',
                        options=options,
                        value=['Atlas'],
                        multi=True,
                        style={'width': '650px'})


