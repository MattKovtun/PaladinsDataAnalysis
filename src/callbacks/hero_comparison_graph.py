from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_comparison_callback(app, tiers, global_store_fn):
    @app.callback(Output('hero-comparison-graph', 'figure'),
                  [Input('hero-dropdown', 'value'),
                   Input('axis-dropdown', 'value'),
                   Input('signal', 'children')])
    def update_hero_comparison_graph(dd_val, y_axe, val):
        dd = global_store_fn(*val)['match']
        dd = dd[dd['hero'].isin(dd_val)]
        dd = dd.groupby(['tier', 'hero'])[y_axe].mean()

        selected_tiers = val[0]
        selected_tiers = range(selected_tiers[0], selected_tiers[1] + 1)

        data = []
        if not dd.empty:
            x = [tiers[i] for i in selected_tiers]
            for h in dd_val:
                tmp_y = [dd[(tier, h)] for tier in selected_tiers]
                data.append(
                    go.Scatter(x=x, y=tmp_y, name=h,
                               showlegend=True, hoverinfo='y',
                               mode='lines'))

        return {
            'data': data,
            'layout': go.Layout(title='Avg stat in won game')}
