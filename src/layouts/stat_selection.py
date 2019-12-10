import dash_core_components as dcc


def stat_selection():
    # TODO: refactor
    options = [{'label': 'Damage taken', 'value': 'damage_taken'},
               {'label': 'Damage done', 'value': 'damage_done'},
               {'label': 'Healing', 'value': 'healing'}]
    return dcc.Dropdown(id='axis-dropdown',
                        options=options,
                        value='damage_done',
                        style={'width': '144px'})


