from .Score import Score

class UserScore(Score):
    def __init__(self, dict):
        self.beatmap_id = dict['beatmap_id']
        self.score_id = dict['score_id']
        self.id = dict['score_id']
        self.date = dict['date']
        self.pp = dict['pp']

    def __str__(self):
        return self.id
