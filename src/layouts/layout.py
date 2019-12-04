import dash_core_components as dcc
import dash_html_components as html


def create_range_slider(df, tiers):
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


def render_layout(df, tiers):
    return html.Div([
        html.Div([
            # html.H4('Paladins ban analysis'),
            dcc.Graph(id='main-graph'),
        ]),

        html.Div([create_range_slider(df, tiers)], style={"width": "95%"}),
        html.Div([
            dcc.Graph(id='hero-graph', style={"width": "50%", "display": "inline-block"}),
            dcc.Graph(id='hero-comparison-graph', style={"width": "50%", "display": "inline-block"})
        ]),
        html.Div([
            html.H4('Observations', style={'text-align': 'center'})
        ])

    ], style={"max-width": "1440px", "margin": "auto"})
