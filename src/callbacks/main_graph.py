import copy

from dash.dependencies import Input, Output
import plotly.graph_objs as go


def main_graph_callback(app, data, global_store_fn):

    @app.callback(Output('main-graph', 'figure'),
                  [Input('signal', 'children')])
    def update_main_graph(val):
        data_selection = global_store_fn(*val)['ban'].groupby('ban').count()['time']
    
        d = copy.deepcopy(data)
        for k in data_selection.keys():
            d[k] = data_selection[k]

        return {
            'data':
                [go.Bar({'x': list(d.keys()), 'y': list(d.values())})],
            'layout': go.Layout(yaxis={'tickformat': ',d'}, title='Paladins ban analysis')}
