from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_graph_callback(app, df, tiers, default_hero):
    @app.callback(Output('hero-graph', 'figure'),
                  [Input('main-graph', 'clickData'),
                   Input('tier-slider', 'value')])
    def update_hero_graph(click, val):
        hero = default_hero
        if click:
            hero = click['points'][0]['label']

        data_selection = df[(df['tier'] >= val[0])
                            & (df['tier'] <= val[1])
                            & (df['ban'] == hero)].groupby('tier').count()['time']

        traces = []

        for k in data_selection.keys():
            traces.append(go.Bar(x=[hero], y=[data_selection[k]], name=tiers[k]))

        return {'data': traces}
