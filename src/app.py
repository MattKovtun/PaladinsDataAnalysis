import dash
import time
from flask_caching import Cache
from dash.dependencies import Input, Output

from utils import prepare_data, create_hero_list
from constants import TIERS, DEFAULT_HERO, MAPS
from layouts.layout import render_layout

from callbacks.hero_graph import hero_graph_callback
from callbacks.main_graph import main_graph_callback
from callbacks.hero_comparison_graph import hero_comparison_callback
from callbacks.hero_dropdown import hero_drop_down_callback
from callbacks.signal import data_selection_callback

app = dash.Dash(__name__)

CACHE_CONFIG = {'CACHE_TYPE': 'filesystem',
                'CACHE_DIR': './cache'}

cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

filename = 'v4.csv'
df = prepare_data("../data/processed/ban_summary/" + filename)
ddf = prepare_data("../data/processed/match_summary/" + filename)

hero_dict = create_hero_list(df)
app.layout = render_layout(df, TIERS, list(hero_dict.keys()), MAPS)


@cache.memoize()
def global_store(tiers, maps):
    # t = time.time()
    ban_summary = df[(df['tier'] >= tiers[0])
                     & (df['tier'] <= tiers[1])]
    ban_summary = ban_summary[ban_summary['map'].isin(maps)]

    match_summary = ddf[(ddf['tier'] >= tiers[0])
                        & (ddf['tier'] <= tiers[1])]
    match_summary = match_summary[match_summary['map'].isin(maps)]

    # print("done", time.time() - t)
    return {'ban': ban_summary, 'match': match_summary}


hero_graph_callback(app, TIERS, DEFAULT_HERO, global_store)
main_graph_callback(app, hero_dict, global_store)
hero_comparison_callback(app, TIERS, global_store)
data_selection_callback(app, global_store)
hero_drop_down_callback(app, DEFAULT_HERO)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)

# refactor code
# add date selection
# add graphic about observations
# rethink csv separation
