import dash_core_components as dcc
import dash_html_components as html

from layouts.main_app.date_picker import date_picker
from layouts.main_app.heroes_dropdown import heroes_dropdown
from layouts.main_app.map_selection import map_selection
from layouts.main_app.range_slider import range_slider
from layouts.main_app.stat_selection import stat_selection


def render_layout(df, tiers, heroes, maps):
    return html.Div([
        html.Div([
            html.Div([
                map_selection(maps),
                date_picker(df),
                html.Span('*match tier = max tier among players', style={'margin-left': '30px'})
            ]),
            dcc.Graph(id='main-graph')]),
        html.Div([range_slider(df, tiers)], style={"width": "95%"}),
        html.Div([
            dcc.Graph(id='hero-graph')], style={"width": "50%", "display": "inline-block"}),
        html.Div([
            html.Div([
                heroes_dropdown(heroes),
                stat_selection(),
            ]),
            dcc.Graph(id='hero-comparison-graph')], style={"width": "50%", "display": "inline-block"}),
        html.Div([
            dcc.Graph(id='observation-graph')
        ]),
        html.Div(id='signal', style={'display': 'none'}),
        html.Div(id='none', children=[], style={'display': 'none'})

    ], style={"max-width": "1440px", "margin": "auto"})
