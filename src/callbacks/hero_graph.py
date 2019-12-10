from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_graph_callback(app, tiers, default_hero, global_store_fn):
    @app.callback(Output('hero-graph', 'figure'),
                  [Input('main-graph', 'clickData'),
                   Input('signal', 'children')])
    def update_hero_graph(click, val):
        hero = default_hero
        if click: hero = click['points'][0]['label']

        dd = global_store_fn(*val)['ban']
        data_selection = dd[dd['ban'] == hero].groupby('tier').count()['time']

        traces = []
        for k in data_selection.keys():
            traces.append(go.Bar(x=[tiers[k]], y=[data_selection[k]], hoverinfo='y'))

        return {'data': traces,
                'layout': go.Layout(title='Bans per tier', showlegend=False)}
