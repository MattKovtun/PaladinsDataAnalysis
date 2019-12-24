# LIMITS
# concurrent_sessions:  50
# sessions_per_day: 500
# session_time_limit:  15 minutes
# request_day_limit:  7500

PALADINS_URL = 'http://api.paladins.com/paladinsapi.svc'
JSON = 'Json'

LANGUAGES = {
    'ENGLISH': '1',
    'GERMAN': '2',
    'FRENCH': '3',
    'SPANISH': '7',
    'SPANISHLA': '9',
    'PORTUGUESE': '10',
    'RUSSIAN': '11',
    'POLISH': '12',
    'TURKISH': '13'}
ENGLISH = LANGUAGES['ENGLISH']

SIEGE = '424'
TDM = '469'
RANKED_SIEGE = '486'

TIER_N = 28
# tier - League tier, unranked = tier 0
TIERS = {1: 'Bronze V',
         2: 'Bronze IV',
         3: 'Bronze III',
         4: 'Bronze II',
         5: 'Bronze I',
         6: 'Silver V',
         7: 'Silver IV',
         8: 'Silver III',
         9: 'Silver II',
         10: 'Silver I',
         11: 'Gold V',
         12: 'Gold IV',
         13: 'Gold III',
         14: 'Gold II',
         15: 'Gold I',
         16: 'Platinum V',
         17: 'Platinum IV',
         18: 'Platinum III',
         19: 'Platinum II',
         20: 'Platinum I',
         21: 'Diamond V',
         22: 'Diamond IV',
         23: 'Diamond III',
         24: 'Diamond II',
         25: 'Diamond I',
         26: 'Masters I',
         27: 'Grandmaster'}

DEFAULT_HERO = 'Atlas'
MAPS = ["Ranked Warder's Gate", 'Ranked Stone Keep', 'Ranked Brightmarsh',
        'Ranked Frog Isle', 'Ranked Jaguar Falls', 'Ranked Ascension Peak',
        'Ranked Serpent Beach', 'Ranked Fish Market', 'Ranked Bazaar',
        'Ranked Splitstone Quarry']

NUMBER_OF_BANS = 4

COLORS = {
    1: 'rgba(148, 97, 66, 0.2)',
    2: 'rgba(148, 97, 66, 0.4)',
    3: 'rgba(148, 97, 66, 0.6000000000000001)',
    4: 'rgba(148, 97, 66, 0.8)',
    5: 'rgba(148, 97, 66, 1.0)',
    6: 'rgba(172, 184, 184, 0.2)',
    7: 'rgba(172, 184, 184, 0.4)',
    8: 'rgba(172, 184, 184, 0.6000000000000001)',
    9: 'rgba(172, 184, 184, 0.8)',
    10: 'rgba(172, 184, 184, 1.0)',
    11: 'rgba(255, 223, 115, 0.2)',
    12: 'rgba(255, 223, 115, 0.4)',
    13: 'rgba(255, 223, 115, 0.6000000000000001)',
    14: 'rgba(255, 223, 115, 0.8)',
    15: 'rgba(255, 223, 115, 1.0)',
    16: 'rgba(200, 113, 244, 0.2)',
    17: 'rgba(200, 113, 244, 0.4)',
    18: 'rgba(200, 113, 244, 0.6000000000000001)',
    19: 'rgba(200, 113, 244, 0.8)',
    20: 'rgba(200, 113, 244, 1.0)',
    21: 'rgba(16, 158, 206, 0.2)',
    22: 'rgba(16, 158, 206, 0.4)',
    23: 'rgba(16, 158, 206, 0.6000000000000001)',
    24: 'rgba(16, 158, 206, 0.8)',
    25: 'rgba(16, 158, 206, 1.0)',
    26: 'rgb(82, 195, 181)',
    27: 'rgb(118, 61, 217)'
}

DEFAULT_COLORMAP = ['#05419b', '#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0',
                    '#f032e6',
                    '#bcf60c',
                    '#fabebe', '#008080', '#e6beff', '#9a6324', '#3588a7', '#fffac8', '#800000', '#aaffc3',
                    '#808000',
                    '#ffd8b1',
                    '#000075', '#808080', '#ffffff', '#000000']
