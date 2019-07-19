class User:
    def __init__(self, dict):
        self.user_id = dict['user_id']
        self.id = dict['user_id']
        self.username = dict['username']
        self.name = dict['username']
        self.join_date = dict['join_date']
        self.count300 = dict['count300']
        self.count100 = dict['count100']
        self.count50 = dict['count50']
        self.playcount = dict['playcount']
        self.ranked_score = dict['ranked_score']
        self.total_score = dict['total_score']
        self.pp_rank = dict['pp_rank']
        self.rank = dict['pp_rank']
        self.level = dict['level']
        self.pp_raw = dict['pp_raw']
        self.pp = dict['pp_raw']
        self.accuracy = dict['accuracy']
        self.count_rank_ss = dict['count_rank_ss']
        self.count_rank_ssh = dict['count_rank_ssh']
        self.count_rank_s = dict['count_rank_s']
        self.count_rank_sh = dict['count_rank_sh']
        self.count_rank_a = dict['count_rank_a']
        self.country = dict['country']
        self.total_seconds_played = dict['total_seconds_played']
        self.country_rank = dict['pp_country_rank']
        events = []
        for event in dict["events"]:
            events.append(UserEvent(event))
        self.events = events

    def __str__(self):
        return self.username


class UserEvent:
    def __init__(self, dict):
        self.display_html = dict['display_html']
        self.beatmap_id = dict['beatmap_id']
        self.beatmapset_id = dict['beatmapset_id']
        self.date = dict['date']
        self.epicfactor = dict['epicfactor']
