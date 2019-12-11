from dash.dependencies import Input, Output


def data_selection_callback(app, global_store_fn):

    @app.callback(Output('signal', 'children'),
                  [Input('tier-slider', 'value'),
                   Input('maps-dropdown', 'value'),
                   Input('date-picker', 'start_date'),
                   Input('date-picker', 'end_date')])
    def compute_value(value, maps, start_date, end_date):
        global_store_fn(value, maps, [start_date, end_date])
        return value, maps, [start_date, end_date]
