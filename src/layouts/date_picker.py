import dash_core_components as dcc


def date_picker(df):
    start_date = df['date'].min()
    end_date = df['date'].max()

    return dcc.DatePickerRange(
        id='date-picker',
        start_date_placeholder_text="Start Period",
        end_date_placeholder_text="End Period",
        start_date=start_date,
        end_date=end_date,
        min_date_allowed=start_date,
        max_date_allowed=end_date,
        reopen_calendar_on_clear=True,
        calendar_orientation='vertical',
    )
