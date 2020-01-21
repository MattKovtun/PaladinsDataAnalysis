import dash_html_components as html
import dash_core_components as dcc
from layouts.secondary_app.heroes_dropdown import heroes_dropdown
from layouts.secondary_app.axis_dropdown import axis_dropdown


def render_layout(heroes):
    return html.Div([
        html.Div(id='_secondary', style={'display': 'hidden'}),
        html.Div([
            heroes_dropdown(heroes),
            axis_dropdown(),
        ]),
        dcc.Graph(id='secondary-hero-comparison-graph'),
    ], id='secondary', style={"max-width": "1440px", "margin": "auto"})
