class MatchPlayer:
    def __init__(self, data):
        self.data = data
        self.match_id = data['Match']
        self.hero = data['Reference_Name']
        self.winner = data['Win_Status'] == 'Winner'
        self.damage_done = data['Damage_Player']
        self.damage_taken = data['Damage_Taken']
        self.healing = data['Healing']
        self.map = data['Map_Game']
        self.tier = data['League_Tier']
        self.time = data['Entry_Datetime']
