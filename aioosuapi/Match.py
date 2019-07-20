class Match:
    def __init__(self, dict):
        self.id = dict['match']['match_id']
        self.match_id = dict['match']['match_id']
        self.name = dict['match']['name']
        self.start_time = dict['match']['start_time']
        self.end_time = dict['match']['end_time']
        games = []
        for game in dict["games"]:
            games.append(Game(game))
        self.games = games

    def __str__(self):
        return self.name


class Game:
    def __init__(self, dict):
        self.game_id = dict['game_id']
        self.start_time = dict['start_time']
        self.end_time = dict['end_time']
        self.beatmap_id = dict['beatmap_id']
        self.play_mode = dict['play_mode']
        self.match_type = dict['match_type']
        self.scoring_type = dict['scoring_type']
        self.team_type = dict['team_type']
        self.mods = dict['mods']
        scores = []
        for score in dict["scores"]:
            scores.append(MultiplayerScore(score))
        self.scores = scores

    def __str__(self):
        return self.beatmap_id


class MultiplayerScore:
    def __init__(self, dict):
        self.slot = dict['slot']
        self.team = dict['team']
        self.user_id = dict['user_id']
        self.score = dict['score']
        self.maxcombo = dict['maxcombo']
        self.rank = dict['rank']
        self.count50 = dict['count50']
        self.count100 = dict['count100']
        self.count300 = dict['count300']
        self.countmiss = dict['countmiss']
        self.countgeki = dict['countgeki']
        self.countkatu = dict['countkatu']
        self.perfect = dict['perfect']
        self.passs = dict['pass']
        self.enabled_mods = dict['enabled_mods']
        self.mods = dict['enabled_mods']
