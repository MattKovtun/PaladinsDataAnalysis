from dash.dependencies import Input, Output


def data_selection_callback(app, global_store_fn):

    @app.callback(Output('signal', 'children'),
                  [Input('tier-slider', 'value'),
                   Input('maps-dropdown', 'value')])
    def compute_value(value, maps):
        global_store_fn(value, maps)
        return value, maps
