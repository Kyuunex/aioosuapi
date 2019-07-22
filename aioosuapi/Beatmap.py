class Beatmap:
    def __init__(self, dict):
        self.approved = dict['approved']
        self.submit_date = dict['submit_date']
        self.approved_date = dict['approved_date']
        self.last_update = dict['last_update']
        self.artist = dict['artist']
        self.beatmap_id = dict['beatmap_id']
        self.id = dict['beatmap_id']
        self.beatmapset_id = dict['beatmapset_id']
        self.bpm = dict['bpm']
        self.creator = dict['creator']
        self.author = dict['creator']
        self.creator_id = dict['creator_id']
        self.difficultyrating = dict['difficultyrating']
        self.diff_aim = dict['diff_aim']
        self.diff_speed = dict['diff_speed']
        self.diff_size = dict['diff_size']
        self.cs = dict['diff_size']
        self.diff_overall = dict['diff_overall']
        self.od = dict['diff_overall']
        self.diff_approach = dict['diff_approach']
        self.ar = dict['diff_approach']
        self.diff_drain = dict['diff_drain']
        self.hp = dict['diff_drain']
        self.hit_length = dict['hit_length']
        self.source = dict['source']
        self.genre_id = dict['genre_id']
        self.language_id = dict['language_id']
        self.title = dict['title']
        self.total_length = dict['total_length']
        self.version = dict['version']
        self.file_md5 = dict['file_md5']
        self.mode = dict['mode']
        self.gamemode = Gamemode(dict['mode'])
        self.tags = dict['tags']
        self.favourite_count = dict['favourite_count']
        self.rating = dict['rating']
        self.playcount = dict['playcount']
        self.passcount = dict['passcount']
        self.count_normal = dict['count_normal']
        self.count_slider = dict['count_slider']
        self.count_spinner = dict['count_spinner']
        self.max_combo = dict['max_combo']
        self.download_unavailable = dict['download_unavailable']
        self.audio_unavailable = dict['audio_unavailable']
        self.thumbnail = "https://b.ppy.sh/thumb/%sl.jpg" % (self.beatmapset_id)
        self.cover = "https://assets.ppy.sh/beatmaps/%s/covers/cover.jpg" % (self.beatmapset_id)
        self.url = "https://osu.ppy.sh/beatmapsets/%s" % (self.beatmapset_id)

    def __str__(self):
        return "%s - %s [%s]" % (self.artist, self.title, self.version)


class Gamemode:
    def __init__(self, mode_id):
        gamemodes = [
            "osu!",
            "Taiko",
            "CtB",
            "osu!mania",
        ]
        self.gamemode = gamemodes[int(mode_id)]

    def __str__(self):
        return self.gamemode