from .MultiplayerGame import MultiplayerGame


class Match:
    def __init__(self, dict):
        self.id = dict['match']['match_id']
        self.match_id = dict['match']['match_id']
        self.name = dict['match']['name']
        self.start_time = dict['match']['start_time']
        self.end_time = dict['match']['end_time']
        games = []
        for game in dict["games"]:
            games.append(MultiplayerGame(game))
        self.games = games

    def __str__(self):
        return self.name
