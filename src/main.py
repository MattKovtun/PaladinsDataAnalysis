import pandas as pd
import dash
import copy
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import prepare_data
from constants import TIERS

app = dash.Dash('Hello World')
df, data = prepare_data("../data/processed/v2.csv")


def create_range_slider():
    uniq = df['tier'].unique()
    mn = min(uniq)
    mx = max(uniq)
    return dcc.RangeSlider(
        id='tier-slider',
        min=mn,
        max=mx,
        marks={int(i): {'label': TIERS[i], 'style': {'color': 'grey'}} for i in uniq},
        value=[mn, mn],
        updatemode='drag')


app.layout = html.Div([
    html.Div([
        html.H4('Paladins ban analysis'),
        dcc.Graph(id='main-graph', config={'displayModeBar': True})]),

    html.Div([create_range_slider()], style={"width": "95%"}),
    html.Div([
        dcc.Graph(id='hero-graph', style={"width": "50%"}),
    ]),

], style={"max-width": "1440px", "margin": "auto"})


@app.callback(Output('hero-graph', 'figure'),
              [Input('main-graph', 'clickData'),
               Input('tier-slider', 'value')])
def update_hero_graph(click, val):
    hero = click['points'][0]['label']

    data_selection = df[(df['tier'] >= val[0])
                        & (df['tier'] <= val[1])
                        & (df['ban'] == hero)].groupby('tier').count()['time']

    traces = []

    for k in data_selection.keys():
        traces.append(go.Bar(x=[hero], y=[data_selection[k]], name=TIERS[k]))

    return {'data': traces,
            'layout': go.Layout()}


@app.callback(Output('main-graph', 'figure'),
              [Input('tier-slider', 'value')])
def update_main_graph(val):
    data_selection = df[(df['tier'] >= val[0]) & (df['tier'] <= val[1])].groupby('ban').count()['time']

    d = copy.deepcopy(data)
    for k in data_selection.keys():
        d[k] = data_selection[k]

    return {
        'data':
            [go.Bar({'x': list(d.keys()), 'y': list(d.values())})],
        'layout': go.Layout(yaxis={'tickformat': ',d'})
    }


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)

# add second graph on click
# refactor code
# add titles
