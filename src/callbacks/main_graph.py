import copy

from dash.dependencies import Input, Output
import plotly.graph_objs as go


def main_graph_callback(app, df, data):
    @app.callback(Output('main-graph', 'figure'),
                  [Input('tier-slider', 'value')])
    def update_main_graph(val):
        data_selection = df[(df['tier'] >= val[0])
                            & (df['tier'] <= val[1])].groupby('ban').count()['time']

        d = copy.deepcopy(data)
        for k in data_selection.keys():
            d[k] = data_selection[k]

        return {
            'data':
                [go.Bar({'x': list(d.keys()), 'y': list(d.values())})],
            'layout': go.Layout(yaxis={'tickformat': ',d'}, title='Paladins ban analysis')}
