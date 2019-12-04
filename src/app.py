import pandas as pd
import dash
import copy
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from utils import prepare_data
from constants import TIERS
from layout import render_layout

app = dash.Dash('Hello World')
df, data = prepare_data("../data/processed/v3.csv")

app.layout = render_layout(df, TIERS)


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

    return {'data': traces}


@app.callback(Output('main-graph', 'figure'),
              [Input('tier-slider', 'value')])
def update_main_graph(val):
    data_selection = df[(df['tier'] >= val[0])
                        & (df['tier'] <= val[1])].groupby('ban').count()['time']

    d = copy.deepcopy(data)
    for k in data_selection.keys():
        d[k] = data_selection[k]

    return {
        'data':
            [go.Bar({'x': list(d.keys()), 'y': list(d.values())})],
        'layout': go.Layout(yaxis={'tickformat': ',d'}, title='Paladins ban analysis')}


@app.callback(Output('hero-comparison-graph', 'figure'),
              [Input('main-graph', 'clickData')])
def update_hero_comparison_graph(click):
    hero = click['points'][0]['label']
    return {'data': []}



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)

# add second graph on click
# refactor code
# add titles
