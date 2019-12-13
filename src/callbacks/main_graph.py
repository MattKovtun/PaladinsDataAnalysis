import copy

from dash.dependencies import Input, Output
import plotly.graph_objs as go


def main_graph_callback(app, data, global_store_fn, default_hero):
    @app.callback(Output('main-graph', 'figure'),
                  [Input('signal', 'children'),
                   Input('main-graph', 'clickData')])
    def update_main_graph(val, click):
        hero = default_hero
        if click: hero = click['points'][0]['label']

        data_selection = global_store_fn(*val)['ban'].groupby('ban').count()['time']

        d = copy.deepcopy(data)
        for k in data_selection.keys():
            d[k] = data_selection[k]

        x = list(d.keys())
        y = list(d.values())
        marker_colors = ['#05419b'] * len(y)
        marker_colors[x.index(hero)] = '#3588a7'

        graph_data = [go.Bar({'x': x, 'y': y, 'marker_color': marker_colors})]

        return {
            'data': graph_data,
            'layout': go.Layout(yaxis={'tickformat': ',d'}, title='Paladins ban analysis')}
