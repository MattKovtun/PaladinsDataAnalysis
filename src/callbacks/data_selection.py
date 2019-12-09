from dash.dependencies import Input, Output


def data_selection_callback(app, global_store_fn):

    @app.callback(Output('signal', 'children'), [Input('tier-slider', 'value')])
    def compute_value(value):
        global_store_fn(value)
        return value
