

from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_comparison_callback(app):
    @app.callback(Output('hero-comparison-graph', 'figure'),
                  [Input('main-graph', 'clickData')])
    def update_hero_comparison_graph(click):
        hero = click['points'][0]['label']
        return {'data': []}
