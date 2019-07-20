from .Accuracy import Accuracy
from .Mod import Mod

class BeatmapScore:
    def __init__(self, dict):
        self.id = dict['score_id']
        self.score_id = dict['score_id']
        self.score = dict['score']
        self.username = dict['username']
        self.count300 = dict['count300']
        self.count100 = dict['count100']
        self.count50 = dict['count50']
        self.countmiss = dict['countmiss']
        self.maxcombo = dict['maxcombo']
        self.countkatu = dict['countkatu']
        self.countgeki = dict['countgeki']
        self.perfect = dict['perfect']
        self.enabled_mods = dict['enabled_mods']
        self.mods = Mod(dict['enabled_mods'])
        self.user_id = dict['user_id']
        self.date = dict['date']
        self.rank = dict['rank']
        self.pp = dict['pp']
        self.replay_available = dict['replay_available']
        self.accuracy = str(Accuracy(self.countmiss, self.count50, self.count100, self.count300))

    def __str__(self):
        return "%s - %spp " % (self.username, self.pp)
