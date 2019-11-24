from .Score import Score


class UserRecentScore(Score):
    def __init__(self, score):
        Score.__init__(self, score)
        self.beatmap_id = score["beatmap_id"]
        self.date = score["date"]

    def __str__(self):
        return self.beatmap_id
