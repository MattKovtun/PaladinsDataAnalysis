import dash
import time
from flask_caching import Cache
from dash.dependencies import Input, Output

from utils import prepare_data, create_hero_list
from constants import TIERS, DEFAULT_HERO
from layouts.layout import render_layout

from callbacks.hero_graph import hero_graph_callback
from callbacks.main_graph import main_graph_callback
from callbacks.hero_comparison_graph import hero_comparison_callback
from callbacks.hero_dropdown import hero_drop_down_callback

app = dash.Dash(__name__)

CACHE_CONFIG = {'CACHE_TYPE': 'filesystem',
                'CACHE_DIR': './cache'}

cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

filename = 'v3.csv'
df = prepare_data("../data/processed/ban_summary/" + filename)
ddf = prepare_data("../data/processed/match_summary/" + filename)

hero_dict = create_hero_list(df)
app.layout = render_layout(df, TIERS, list(hero_dict.keys()))


@cache.memoize()
def global_store(tiers):
    t = time.time()
    data_selection = df[(df['tier'] >= tiers[0])
                        & (df['tier'] <= tiers[1])]
    print("done", time.time() - t)
    return data_selection


@app.callback(Output('signal', 'children'), [Input('tier-slider', 'value')])
def compute_value(value):
    global_store(value)
    return value


hero_graph_callback(app, df, TIERS, DEFAULT_HERO)
main_graph_callback(app, hero_dict, global_store)
hero_comparison_callback(app, TIERS, global_store)
hero_drop_down_callback(app, DEFAULT_HERO)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)

# Doing refactor using caching and signaling
# refactor code
# add map selection
# add date selection
# add 3d graph
