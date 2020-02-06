from dash.dependencies import Input, Output, State
import plotly.graph_objs as go


def secondary_pickrate_callback(app, pickrate, default_colormap):
    @app.callback(Output('secondary-pickrate', 'figure'),
                  [Input('secondary-hero-dropdown', 'value')])
    def pickrate_calc(heroes):
        h = [i[0] for i in pickrate]
        p = [i[1] for i in pickrate]
        colors = [default_colormap[0]] * len(h)
        for i in heroes: colors[h.index(i)] = default_colormap[2]
        return {'data': [go.Scatter(x=h,
                                    y=p,
                                    mode='markers',
                                    marker_color=colors,
                                    marker=dict(size=9)
                                    )],

                'layout': go.Layout(yaxis={},
                                    title='Hero pick rate')}

    @app.callback(Output('secondary-hero-dropdown', 'value'),
                  [Input('secondary-pickrate', 'clickData')],
                  [State('secondary-hero-dropdown', 'value')])
    def update_dd(click, vals):
        hero = click['points'][0]['x']
        vals.append(hero)
        return vals
