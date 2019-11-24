from .Accuracy import Accuracy
from .Mod import Mod


class Score:
    def __init__(self, score):
        self.user_id = score["user_id"]
        self.score = score["score"]
        self.maxcombo = score["maxcombo"]
        self.max_combo = score["maxcombo"]
        self.count50 = score["count50"]
        self.count100 = score["count100"]
        self.count300 = score["count300"]
        self.countmiss = score["countmiss"]
        self.count_miss = score["countmiss"]
        self.countkatu = score["countkatu"]
        self.count_katu = score["countkatu"]
        self.countgeki = score["countgeki"]
        self.count_geki = score["countgeki"]
        self.perfect = score["perfect"]
        self.rank = score["rank"]
        self.enabled_mods = score["enabled_mods"]
        self.mods = Mod(score["enabled_mods"])
        self.accuracy = str(Accuracy(self.countmiss, self.count50, self.count100, self.count300))

    def __str__(self):
        return self.user_id
