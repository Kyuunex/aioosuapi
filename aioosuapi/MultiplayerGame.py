from .MultiplayerScore import MultiplayerScore


class MultiplayerGame:
    def __init__(self, dict):
        self.game_id = dict['game_id']
        self.start_time = dict['start_time']
        self.end_time = dict['end_time']
        self.beatmap_id = dict['beatmap_id']
        self.play_mode = dict['play_mode']
        self.match_type = dict['match_type']
        self.scoring_type = dict['scoring_type']
        self.team_type = dict['team_type']
        self.mods = dict['mods']
        scores = []
        for score in dict["scores"]:
            scores.append(MultiplayerScore(score))
        self.scores = scores

    def __str__(self):
        return self.beatmap_id