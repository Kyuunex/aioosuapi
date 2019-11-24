from .Score import Score


class BeatmapScore(Score):
    def __init__(self, score):
        Score.__init__(self, score)
        self.id = score["score_id"]
        self.score_id = score["score_id"]
        self.username = score["username"]
        self.date = score["date"]
        self.pp = score["pp"]
        self.replay_available = score["replay_available"]

    def __str__(self):
        return f"{self.username} - {self.pp}pp"
