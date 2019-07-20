from .Accuracy import Accuracy
from .Mod import Mod

class UserRecentScore:
    def __init__(self, dict):
        self.beatmap_id = dict['beatmap_id']
        self.score = dict['score']
        self.maxcombo = dict['maxcombo']
        self.count50 = dict['count50']
        self.count100 = dict['count100']
        self.count300 = dict['count300']
        self.countmiss = dict['countmiss']
        self.countkatu = dict['countkatu']
        self.countgeki = dict['countgeki']
        self.perfect = dict['perfect']
        self.enabled_mods = dict['enabled_mods']
        self.mods = Mod(dict['enabled_mods'])
        self.user_id = dict['user_id']
        self.date = dict['date']
        self.rank = dict['rank']
        self.accuracy = str(Accuracy(self.countmiss, self.count50, self.count100, self.count300))

    def __str__(self):
        return self.beatmap_id
