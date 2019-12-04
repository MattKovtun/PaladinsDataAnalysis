import dash
import copy
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from utils import prepare_data
from constants import TIERS
from layout import render_layout

from callbacks.hero_graph import hero_graph_callback
from callbacks.main_graph import main_graph_callback
from callbacks.hero_comparison_graph import hero_comparison_callback

app = dash.Dash('Hello World')
df, data = prepare_data("../data/processed/v3.csv")

app.layout = render_layout(df, TIERS)

hero_graph_callback(app, df, TIERS)
main_graph_callback(app, df, data)
hero_comparison_callback(app)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)

# add second graph on click
# refactor code
# add titles
