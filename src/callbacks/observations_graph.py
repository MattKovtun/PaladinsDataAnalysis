from dash.dependencies import Output, Input
import plotly.graph_objs as go


def observations_callback(app, number_of_bans, tiers, global_store_fn):
    @app.callback(Output('observation-graph', 'figure'),
                  [Input('signal', 'children')])
    def update_observation_graph(_):
        df = global_store_fn(*_)['ban']
        data = (df.groupby('tier').count() / number_of_bans)['ban']

        return {'data': [go.Scatter(x=[tiers[i] for i in data.keys()],
                                    y=data.values,
                                    mode='lines+markers', hoverinfo='y')],

                'layout': go.Layout(yaxis={'tickformat': ',d'},
                                    title='Matches per tier')}
