from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_comparison_callback(app, tiers, global_store_fn):
    @app.callback(Output('hero-comparison-graph', 'figure'),
                  [Input('hero-dropdown', 'value'),
                   Input('axis-dropdown', 'value'),
                   Input('signal', 'children')])
    def update_hero_comparison_graph(dd_val, y_axe, val):
        data_selection = global_store_fn(val)
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
            'layout': go.Layout(yaxis={'tickformat': ',d'}, title='Avg stat in won game')}
