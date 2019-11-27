class Match:
    def __init__(self, data):
        self.data = data
        self.number_of_players = len(self.data)

    def get_bans(self):
        player = self.data[0]  # they all are the same
        number_of_bans = 4     # in current patch it's constant
        hero_id = 'BanId'
        hero_name = 'Ban_'

        bans = dict()
        for i in range(1, number_of_bans + 1):
            bans[player[hero_name + str(i)]] = player[hero_id + str(i)]

        return bans

    def get_league_tiers(self):
        league_tier = 'League_Tier'

        league_tiers = [-1] * self.number_of_players

        for i in range(self.number_of_players):
            league_tiers[i] = self.data[i][league_tier]

        return league_tiers

    def get_time(self):
        return self.data[0]["Entry_Datetime"]


