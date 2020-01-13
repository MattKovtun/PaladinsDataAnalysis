import dash_html_components as html


def render_layout():
    return html.Div([
        html.Div(id='_secondary', style={'display': 'hidden'})
    ], id='secondary', style={"max-width": "1440px", "margin": "auto"})
