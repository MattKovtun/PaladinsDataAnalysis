import dash

from utils import prepare_data, create_hero_list
from constants import TIERS, DEFAULT_HERO
from layouts.layout import render_layout

from callbacks.hero_graph import hero_graph_callback
from callbacks.main_graph import main_graph_callback
from callbacks.hero_comparison_graph import hero_comparison_callback
from callbacks.hero_dropdown import hero_drop_down_callback

app = dash.Dash('Hello World')

filename = 'v3.csv'
df = prepare_data("../data/processed/ban_summary/" + filename)
ddf = prepare_data("../data/processed/match_summary/" + filename)

hero_dict = create_hero_list(df)
app.layout = render_layout(df, TIERS, list(hero_dict.keys()))

hero_graph_callback(app, df, TIERS, DEFAULT_HERO)
main_graph_callback(app, df, hero_dict)
hero_comparison_callback(app, ddf, TIERS)
hero_drop_down_callback(app, DEFAULT_HERO)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)

# refactor using caching and signaling
# refactor code
# add map selection
# add date selection
# add 3d graph
