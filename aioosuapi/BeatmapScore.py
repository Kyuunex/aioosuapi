from .Score import Score


class BeatmapScore(Score):
    def __init__(self, dict):
        Score.__init__(self, dict)
        self.id = dict['score_id']
        self.score_id = dict['score_id']
        self.username = dict['username']
        self.date = dict['date']
        self.pp = dict['pp']
        self.replay_available = dict['replay_available']

    def __str__(self):
        return "%s - %spp " % (self.username, self.pp)
