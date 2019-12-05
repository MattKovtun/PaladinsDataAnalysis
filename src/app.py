import dash

from utils import prepare_data, create_hero_list
from constants import TIERS
from layouts.layout import render_layout

from callbacks.hero_graph import hero_graph_callback
from callbacks.main_graph import main_graph_callback
from callbacks.hero_comparison_graph import hero_comparison_callback

app = dash.Dash('Hello World')

filename = 'v3.csv'
df = prepare_data("../data/processed/ban_summary/" + filename)
hero_list = create_hero_list(df)

app.layout = render_layout(df, TIERS)

hero_graph_callback(app, df, TIERS)
main_graph_callback(app, df, hero_list)
hero_comparison_callback(app)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)


# refactor code
# add map selection
# add date selection
# add 3d graph
