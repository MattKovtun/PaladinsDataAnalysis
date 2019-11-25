class Match:
    def __init__(self, match_info):
        self.match_info = match_info

    def get_bans(self):
        player = self.match_info[0]
        number_of_bans = 4
        hero_id = 'BanId'
        hero_name = 'Ban_'

        bans = dict()
        for i in range(1, number_of_bans + 1):
            bans[player[hero_name + str(i)]] = player[hero_id + str(i)]

        return bans



