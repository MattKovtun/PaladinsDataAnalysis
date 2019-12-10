from dash.dependencies import Output, Input
import plotly.graph_objs as go


def observations_callback(app, df, number_of_bans, tiers):
    @app.callback(Output('observation-graph', 'figure'),
                  [Input('none', 'children')])
    def update_hero_graph(_):
        data = (df.groupby('tier').count() / number_of_bans)['ban']

        return {'data': [go.Scatter(x=[tiers[i] for i in data.keys()], y=data.values,
                                    mode='lines+markers',)],
                'layout': go.Layout(yaxis={'tickformat': ',d'}, title='Matches per tier')}
