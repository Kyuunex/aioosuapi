from .Score import Score

class UserRecentScore(Score):
    def __init__(self, dict):
        Score.__init__(self, dict)
        self.beatmap_id = dict['beatmap_id']
        self.date = dict['date']

    def __str__(self):
        return self.beatmap_id
