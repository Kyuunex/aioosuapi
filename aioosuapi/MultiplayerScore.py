from .Score import Score


class MultiplayerScore(Score):
    def __init__(self, dict):
        Score.__init__(self, dict)
        self.slot = dict['slot']
        self.team = dict['team']
        self.passs = dict['pass']
