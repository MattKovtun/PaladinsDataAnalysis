from dash.dependencies import Input, Output


def secondary_page_callback(app):
    @app.callback(Output('secondary', 'children'),
                  [Input('_secondary', 'value')])
    def update_hero_comparison_graph(_):
        return "asd"
