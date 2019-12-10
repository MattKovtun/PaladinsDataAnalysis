from paladins_api.constants import NUMBER_OF_BANS


class Match:
    def __init__(self, data):
        self.data = data
        self.number_of_players = len(self.data)

    @property
    def get_bans(self):
        player = self.data[0]  # they all are the same
        number_of_bans = NUMBER_OF_BANS
        hero_id = 'BanId'
        hero_name = 'Ban_'

        bans = dict()
        for i in range(1, number_of_bans + 1):
            bans[player[hero_name + str(i)]] = player[hero_id + str(i)]

        return bans

    @property
    def get_league_tiers(self):
        league_tier = 'League_Tier'

        league_tiers = [-1] * self.number_of_players

        for i in range(self.number_of_players):
            league_tiers[i] = self.data[i][league_tier]

        return league_tiers

    @property
    def get_match_id(self):
        return self.data[0]['Match']

    @property
    def get_time(self):
        return self.data[0]['Entry_Datetime']

    @property
    def get_map(self):
        return self.data[0]['Map_Game']
