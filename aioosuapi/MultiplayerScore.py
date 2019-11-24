from .Score import Score


class MultiplayerScore(Score):
    def __init__(self, score):
        Score.__init__(self, score)
        self.slot = score["slot"]
        self.team = score["team"]
        self.passs = score["pass"]
