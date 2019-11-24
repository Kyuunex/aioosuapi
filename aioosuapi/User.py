from .UserEvent import UserEvent


class User:
    def __init__(self, user):
        self.user_id = user["user_id"]
        self.id = user["user_id"]
        self.username = user["username"]
        self.name = user["username"]
        self.join_date = user["join_date"]
        self.count300 = user["count300"]
        self.count100 = user["count100"]
        self.count50 = user["count50"]
        self.playcount = user["playcount"]
        self.play_count = user["playcount"]
        self.ranked_score = user["ranked_score"]
        self.total_score = user["total_score"]
        self.pp_rank = user["pp_rank"]
        self.rank = user["pp_rank"]
        self.level = user["level"]
        self.pp_raw = user["pp_raw"]
        self.pp = user["pp_raw"]
        self.accuracy = user["accuracy"]
        self.count_rank_ss = user["count_rank_ss"]
        self.count_rank_ssh = user["count_rank_ssh"]
        self.count_rank_s = user["count_rank_s"]
        self.count_rank_sh = user["count_rank_sh"]
        self.count_rank_a = user["count_rank_a"]
        self.country = user["country"]
        self.total_seconds_played = user["total_seconds_played"]
        self.country_rank = user["pp_country_rank"]
        self.avatar = f"https://a.ppy.sh/{self.user_id}"
        self.url = f"https://osu.ppy.sh/users/{self.user_id}"
        events = []
        for event in user["events"]:
            events.append(UserEvent(event))
        self.events = events

    def __str__(self):
        return self.username
