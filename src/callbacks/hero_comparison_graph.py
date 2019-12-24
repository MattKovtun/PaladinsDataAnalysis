from dash.dependencies import Input, Output
import plotly.graph_objs as go


def hero_comparison_callback(app, tiers, global_store_fn, default_colormap):
    @app.callback(Output('hero-comparison-graph', 'figure'),
                  [Input('hero-dropdown', 'value'),
                   Input('axis-dropdown', 'value'),
                   Input('tier-slider', 'value'),
                   Input('signal', 'children')])
    def update_hero_comparison_graph(dd_heroes, y_axe, selected_tiers, _):
        data = global_store_fn(*_)['match']
        data = data[data['hero'].isin(dd_heroes)]

        min_tier, max_tier = selected_tiers
        x = [tiers[i] for i in tiers][min_tier - 1:max_tier]

        if y_axe == 'win_rate':
            scatter_data = calc_win_rate(data, dd_heroes, selected_tiers)
        else:
            scatter_data = select_field(data, y_axe, dd_heroes)
        return {
            'data': [go.Scatter(x=x,
                                y=scatter_data[hero][min_tier - 1:max_tier], name=hero,
                                showlegend=True, hoverinfo='y',
                                mode='lines+markers',
                                marker_color=default_colormap[i % len(default_colormap)]
                                ) for i, hero in enumerate(scatter_data)],
            'layout': go.Layout(title='Avg stat in won game',
                                )}

    def select_field(data, y_axe, dd_heroes):
        data = data.groupby(['tier', 'hero'])[y_axe].mean()
        scatter_data = {hero: [None] * (len(tiers)) for hero in dd_heroes}

        for (tier, hero) in data.keys():
            if hero in scatter_data:
                scatter_data[hero][tier - 1] = data[(tier, hero)]
        return scatter_data

    def calc_win_rate(df, dd_heroes, selected_tiers):
        # don't recalc for all
        scatter_data = {hero: [None] * (len(tiers)) for hero in dd_heroes}
        for hero in dd_heroes:
            for tier in range(selected_tiers[0], selected_tiers[1] + 1):
                total = df[(df['hero'] == hero)
                           & (df['tier'] == tier)]
                wins = total[total['winner']].shape[0]
                total = total.shape[0]

                if total:
                    scatter_data[hero][tier - 1] = wins / total
        return scatter_data
