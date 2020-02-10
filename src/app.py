import dash
import dash_core_components as dcc
import dash_html_components as html
from flask_caching import Cache
from dash.dependencies import Input, Output

from datetime import datetime
from utils import prepare_data, create_hero_list, calc_ban_rate, calc_pick_rate
from constants import TIERS, DEFAULT_HERO, MAPS, NUMBER_OF_BANS
from constants import COLORS, DEFAULT_COLORMAP, CACHE_CONFIG, BAN_SUMMARY, MATCH_SUMMARY
from layouts.main_app.layout import render_layout

from callbacks.main_app.bans_per_tier_graph import hero_graph_callback
from callbacks.main_app.ban_graph import main_graph_callback
from callbacks.main_app.hero_comparison_graph import hero_comparison_callback
from callbacks.main_app.hero_comparison_dropdown import hero_drop_down_callback
from callbacks.main_app.signal import data_selection_callback
from callbacks.main_app.observations_graph import observations_callback

from layouts.secondary_app.layout import render_layout as rl2

from callbacks.secondary_app.over_time import secondary_app_callback
from callbacks.secondary_app.pickrate import secondary_pickrate_callback

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions'] = True

cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

df = prepare_data(BAN_SUMMARY)
ddf = prepare_data(MATCH_SUMMARY)
pickrate = calc_pick_rate(ddf, df)
banrate = calc_ban_rate(df)

hero_dict = create_hero_list(df)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return render_layout(df, TIERS, list(hero_dict.keys()), MAPS)
    elif pathname == '/stats':
        return rl2(list(hero_dict.keys()))
    else:
        return '404'


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
main_graph_callback(app, hero_dict, global_store, DEFAULT_HERO, DEFAULT_COLORMAP)
hero_comparison_callback(app, TIERS, global_store, DEFAULT_COLORMAP)
data_selection_callback(app, global_store)
hero_drop_down_callback(app, DEFAULT_HERO)
observations_callback(app, NUMBER_OF_BANS, TIERS, global_store, DEFAULT_COLORMAP)

secondary_app_callback(app, TIERS, ddf, DEFAULT_COLORMAP)
secondary_pickrate_callback(app, pickrate, banrate, DEFAULT_COLORMAP)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)

# refactor code, add config
# setup cron job, consider rewriting to factory
