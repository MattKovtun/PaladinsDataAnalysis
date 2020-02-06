from dash.dependencies import Input, Output, State
import plotly.graph_objs as go


def secondary_pickrate_callback(app, pickrate, banrate, default_colormap):
    @app.callback(Output('secondary-pickrate', 'figure'),
                  [Input('secondary-hero-dropdown', 'value'),
                   Input('secondary-checklist', 'value')])
    def pickrate_calc(heroes, checklist):
        d = {'bans': [banrate, 'rgba(60, 180, 75, .3)', 'rgb(60, 180, 75)'],
             'picks': [pickrate, 'rgba(5, 65, 155, .3)', 'rgb(5, 65, 155)']}

        def create_scatter(t):
            h = [i[0] for i in d[t][0]]
            p = [i[1] for i in d[t][0]]
            colors = [d[t][1]] * len(h)
            for i in heroes: colors[h.index(i)] = d[t][2]
            return go.Scatter(x=h,
                              y=p,
                              mode='markers',
                              marker_color=colors,
                              marker=dict(size=8.5),
                              name=t)

        return {'data': [create_scatter(i) for i in checklist],
                'layout': go.Layout(yaxis={},
                                    title='Hero pick&ban rate')}

    @app.callback(Output('secondary-hero-dropdown', 'value'),
                  [Input('secondary-pickrate', 'clickData')],
                  [State('secondary-hero-dropdown', 'value')])
    def update_dd(click, vals):
        hero = click['points'][0]['x']
        vals.append(hero)
        return vals
