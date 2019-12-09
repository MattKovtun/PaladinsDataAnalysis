from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_comparison_callback(app, df, tiers):
    @app.callback(Output('hero-comparison-graph', 'figure'),
                  [Input('tier-slider', 'value'),
                   Input('hero-dropdown', 'value'),
                   Input('axis-dropdown', 'value')])
    def update_hero_comparison_graph(val, dd_val, y_axe):
        data_selection = df[(df['tier'] >= val[0])
                            & (df['tier'] <= val[1])]

        data_selection = data_selection[data_selection['hero'].isin(dd_val)]
        dd = data_selection.groupby(['tier', 'hero'])[y_axe].mean()
        selected_tiers = range(val[0], val[1] + 1)

        y = []
        x = [tiers[i] for i in selected_tiers]
        for h in dd_val:
            tmp_y = []
            for tier in selected_tiers:
                tmp_y.append(dd[(tier, h)])
            y.append(tmp_y)

        return {
            'data':
                [go.Scatter(x=x, y=j, name=dd_val[i], showlegend=True) for i, j in enumerate(y)],
            'layout': go.Layout(yaxis={'tickformat': ',d'})}
