import pandas as pd
import dash
import copy
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash('Hello World')

df = pd.read_csv("../data/processed/v1.csv")
df['time'] = pd.to_datetime(df['time'])
df['date'] = df['time'].dt.date
x = df['ban'].unique()
x.sort()
y = [0] * len(x)
data = dict(zip(x, y))


def create_range_slider():
    uniq = df['tier'].unique()
    mn = min(uniq)
    mx = max(uniq)
    return dcc.RangeSlider(
        id='slider',
        min=mn,
        max=mx,
        marks={int(i): str(i) for i in uniq},
        value=[mn, mn],
        updatemode='drag')


app.layout = html.Div([
    html.Div([
        dcc.Graph(id='my-graph',
                  config={
                      'displayModeBar': True}),
    ]),

    html.Div([create_range_slider()],
             style={"width": "95%"})],
    style={"max-width": "1440px", "margin": "auto"})


@app.callback(Output('my-graph', 'figure'),
              [Input('slider', 'value')])
def update_graph(val):
    data_selection = df[(df['tier'] >= val[0]) & (df['tier'] <= val[1])].groupby('ban').count()['time']

    d = copy.deepcopy(data)
    for k in data_selection.keys():
        d[k] = data_selection[k]

    return {
        'data':
            [go.Bar({'x': list(d.keys()), 'y': list(d.values())})]
    }


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
