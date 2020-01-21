from dash.dependencies import Input, Output
import plotly.graph_objs as go


def secondary_app_callback(app, tiers, df, default_colormap):
    def select_field(data, y_axe, dd_heroes):
        data = data.groupby(['tier', 'hero'])[y_axe]
        mean = data.mean()
        count = data.count()
        scatter_data = {hero: [None] * (len(tiers)) for hero in dd_heroes}
        text_data = {hero: [None] * (len(tiers)) for hero in dd_heroes}

        for (tier, hero) in mean.keys():
            if hero in scatter_data:
                scatter_data[hero][tier - 1] = mean[(tier, hero)]
                text_data[hero][tier - 1] = str(count[(tier, hero)]) + ' games'
        return scatter_data, text_data

    @app.callback(Output('secondary-hero-comparison-graph', 'figure'),
                  [Input('secondary-hero-dropdown', 'value'),
                   Input('secondary-axis-dropdown', 'value')])
    def update_hero_comparison_graph(dd_heroes, y_axe):
        data = df[df['hero'].isin(dd_heroes)]

        min_tier = min(tiers)
        max_tier = max(tiers)
        x = [tiers[i] for i in tiers][min_tier - 1:max_tier]

        scatter_data, text_data = select_field(data, y_axe, dd_heroes)
        return {
            'data': [go.Scatter(x=x,
                                y=scatter_data[hero][min_tier - 1:max_tier], name=hero,
                                showlegend=True, hoverinfo='y+text',
                                mode='lines+markers',
                                marker_color=default_colormap[i % len(default_colormap)],
                                text=text_data[hero][min_tier - 1: max_tier]
                                ) for i, hero in enumerate(scatter_data)],
            'layout': go.Layout(title='Avg stat in won game')}
