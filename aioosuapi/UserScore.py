from .Score import Score


class UserScore(Score):
    def __init__(self, score):
        Score.__init__(self, score)
        self.beatmap_id = score["beatmap_id"]
        self.score_id = score["score_id"]
        self.id = score["score_id"]
        self.date = score["date"]
        self.pp = score["pp"]

    def __str__(self):
        return self.id
