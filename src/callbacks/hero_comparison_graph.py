from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_comparison_callback(app, df, tiers):
    @app.callback(Output('hero-comparison-graph', 'figure'),
                  [Input('main-graph', 'clickData'),
                   Input('tier-slider', 'value')])
    def update_hero_comparison_graph(click, val):
        hero = click['points'][0]['label']
        data_selection = df[(df['tier'] >= val[0])
                            & (df['tier'] <= val[1])]

        dd = data_selection[data_selection['hero'] == hero].groupby('tier')['damage_taken'].mean()

        x = []
        y = []
        for k in dd.keys():
            x.append(tiers[k])
            y.append(dd[k])

        return {
            'data':
                [go.Scatter(x=x, y=y)],
            'layout': go.Layout(yaxis={'tickformat': ',d'})}
