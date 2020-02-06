import dash_core_components as dcc


def axis_dropdown():
    options = [{'label': 'Damage taken', 'value': 'damage_taken'},
               {'label': 'Damage done', 'value': 'damage_done'},
               {'label': 'Healing', 'value': 'healing'},
               {'label': 'Win rate', 'value': 'win_rate'}]
    return dcc.Dropdown(id='secondary-axis-dropdown',
                        options=options,
                        value='damage_done',
                        style={'width': '144px'})
