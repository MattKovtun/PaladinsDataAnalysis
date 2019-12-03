from etl.data_transformation import read_tier, form_csv, get_match_info
from etl.match_scrapper import matches_to_tiers, scrap_ranked_matches


from paladins_api.basic_api import BasicApi
from dev_creds import DEV_ID, AUTH_KEY


api = BasicApi(DEV_ID, AUTH_KEY)





