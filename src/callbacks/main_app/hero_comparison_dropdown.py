from dash.dependencies import Input, Output


def hero_drop_down_callback(app, default_hero):

    @app.callback(Output('hero-dropdown', 'value'),
                  [Input('main-graph', 'clickData'),
                   Input('signal', 'children')])
    def update_hero_comparison_graph(click, _):
        hero = default_hero
        if click:
            hero = click['points'][0]['label']
        return [hero]
