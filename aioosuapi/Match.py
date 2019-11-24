from .MultiplayerGame import MultiplayerGame


class Match:
    def __init__(self, match):
        self.id = match["match"]["match_id"]
        self.match_id = match["match"]["match_id"]
        self.name = match["match"]["name"]
        self.start_time = match["match"]["start_time"]
        self.end_time = match["match"]["end_time"]
        games = []
        for game in match["games"]:
            games.append(MultiplayerGame(game))
        self.games = games

    def __str__(self):
        return self.name
