from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_comparison_callback(app, tiers, global_store_fn):
    @app.callback(Output('hero-comparison-graph', 'figure'),
                  [Input('hero-dropdown', 'value'),
                   Input('axis-dropdown', 'value'),
                   Input('tier-slider', 'value'),
                   Input('signal', 'children')])
    def update_hero_comparison_graph(dd_heroes, y_axe, selected_tiers, _):
        data = global_store_fn(*_)['match']
        data = data[data['hero'].isin(dd_heroes)]
        data = data.groupby(['tier', 'hero'])[y_axe].mean()

        min_tier, max_tier = selected_tiers
        scatter_data = {hero: [None] * (len(tiers)) for hero in dd_heroes}

        for (tier, hero) in data.keys():
            if hero in scatter_data:
                scatter_data[hero][tier - 1] = data[(tier, hero)]  # ranks are 1-based

        x = [tiers[i] for i in tiers][min_tier:max_tier]
        return {
            'data': [go.Scatter(x=x,
                                y=scatter_data[hero][min_tier:max_tier], name=hero,
                                showlegend=True, hoverinfo='y',
                                mode='lines+markers') for hero in scatter_data],
            'layout': go.Layout(title='Avg stat in won game',
                                )}
