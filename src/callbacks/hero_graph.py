from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_graph_callback(app, tiers, default_hero, global_store_fn, colors):
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
            traces.append(
                go.Bar(x=[tiers[k]], y=[data_selection[k]], hoverinfo='x+y+text', marker_color=colors[k], text=hero))

        return {'data': traces,
                'layout': go.Layout(title='Bans per tier', showlegend=False, xaxis=dict(showticklabels=False))}
