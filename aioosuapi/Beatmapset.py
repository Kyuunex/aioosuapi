from .Beatmap import Beatmap


class Beatmapset:
    def __init__(self, list):
        dict = list[0]
        self.approved = dict['approved']
        self.submit_date = dict['submit_date']
        self.approved_date = dict['approved_date']
        self.last_update = dict['last_update']
        self.artist = dict['artist']
        self.id = dict['beatmapset_id']
        self.beatmapset_id = dict['beatmapset_id']
        self.bpm = dict['bpm']
        self.creator = dict['creator']
        self.author = dict['creator']
        self.creator_id = dict['creator_id']
        self.source = dict['source']
        self.genre_id = dict['genre_id']
        self.language_id = dict['language_id']
        self.title = dict['title']
        self.total_length = dict['total_length']
        self.tags = dict['tags']
        self.favourite_count = dict['favourite_count']
        self.rating = dict['rating']
        self.download_unavailable = dict['download_unavailable']
        self.audio_unavailable = dict['audio_unavailable']
        self.thumbnail = "https://b.ppy.sh/thumb/%sl.jpg" % (self.beatmapset_id)
        self.cover = "https://assets.ppy.sh/beatmaps/%s/covers/cover.jpg" % (self.beatmapset_id)
        self.url = "https://osu.ppy.sh/beatmapsets/%s" % (self.beatmapset_id)
        self.direct = "osu://dl/%s" % (self.beatmapset_id)
        beatmaps = []
        for beatmap in list:
            beatmaps.append(Beatmap(beatmap))
        self.beatmaps = beatmaps

    def __str__(self):
        return "%s - %s (%s)" % (self.artist, self.title, self.creator)
