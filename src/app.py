import dash
import time
from flask_caching import Cache
from dash.dependencies import Input, Output

from datetime import datetime
from utils import prepare_data, create_hero_list
from constants import TIERS, DEFAULT_HERO, MAPS, NUMBER_OF_BANS, COLORS
from layouts.layout import render_layout

from callbacks.hero_graph import hero_graph_callback
from callbacks.main_graph import main_graph_callback
from callbacks.hero_comparison_graph import hero_comparison_callback
from callbacks.hero_dropdown import hero_drop_down_callback
from callbacks.signal import data_selection_callback
from callbacks.observations_graph import observations_callback

app = dash.Dash(__name__)

CACHE_CONFIG = {'CACHE_TYPE': 'filesystem',
                'CACHE_DIR': './cache'}

cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

filename = 'v5.csv'
df = prepare_data("../data/processed/ban_summary/" + filename)
ddf = prepare_data("../data/processed/match_summary/" + filename)

hero_dict = create_hero_list(df)
app.layout = render_layout(df, TIERS, list(hero_dict.keys()), MAPS)


@cache.memoize()
def global_store(tiers, maps, dates):
    def select_data(data):
        data = data[(data['tier'] >= tiers[0])
                    & (data['tier'] <= tiers[1])
                    & (data['date'] >= start_end)
                    & (data['date'] < end_date)
                    ]
        return data[data['map'].isin(maps)]

    start_end = datetime.strptime(dates[0], '%Y-%m-%d').date()
    end_date = datetime.strptime(dates[1], '%Y-%m-%d').date()

    # t = time.time()
    ban_summary = select_data(df)
    match_summary = select_data(ddf)
    # print("done", time.time() - t)
    return {'ban': ban_summary, 'match': match_summary}


hero_graph_callback(app, TIERS, DEFAULT_HERO, global_store, COLORS)
main_graph_callback(app, hero_dict, global_store)
hero_comparison_callback(app, TIERS, global_store)
data_selection_callback(app, global_store)
hero_drop_down_callback(app, DEFAULT_HERO)
observations_callback(app, NUMBER_OF_BANS, TIERS, global_store)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)

# refactor code
# add click main graph
