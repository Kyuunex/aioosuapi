from .MultiplayerScore import MultiplayerScore


class MultiplayerGame:
    def __init__(self, game):
        self.game_id = game["game_id"]
        self.start_time = game["start_time"]
        self.end_time = game["end_time"]
        self.beatmap_id = game["beatmap_id"]
        self.play_mode = game["play_mode"]
        self.match_type = game["match_type"]
        self.scoring_type = game["scoring_type"]
        self.team_type = game["team_type"]
        self.mods = game["mods"]
        scores = []
        for score in game["scores"]:
            scores.append(MultiplayerScore(score))
        self.scores = scores

    def __str__(self):
        return self.beatmap_id
