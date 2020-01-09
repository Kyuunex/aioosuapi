from .Beatmap import Beatmap


class Beatmapset:
    def __init__(self, diffs):
        diff = diffs[0]
        self.approved = diff["approved"]
        self.submit_date = diff["submit_date"]
        self.approved_date = diff["approved_date"]
        self.last_update = diff["last_update"]
        self.artist = diff["artist"]
        self.id = diff["beatmapset_id"]
        self.beatmapset_id = diff["beatmapset_id"]
        self.bpm = diff["bpm"]
        self.creator = diff["creator"]
        self.author = diff["creator"]
        self.creator_id = diff["creator_id"]
        self.source = diff["source"]
        self.genre_id = diff["genre_id"]
        self.language_id = diff["language_id"]
        self.title = diff["title"]
        self.total_length = diff["total_length"]
        self.tags = diff["tags"]
        self.favourite_count = diff["favourite_count"]
        self.rating = diff["rating"]
        self.download_unavailable = diff["download_unavailable"]
        self.audio_unavailable = diff["audio_unavailable"]
        self.thumbnail = f"https://b.ppy.sh/thumb/{self.beatmapset_id}l.jpg"
        self.thumb = f"https://assets.ppy.sh/beatmaps/{self.beatmapset_id}/covers/list@2x.jpg"
        self.cover = f"https://assets.ppy.sh/beatmaps/{self.beatmapset_id}/covers/cover.jpg"
        self.url = f"https://osu.ppy.sh/beatmapsets/{self.beatmapset_id}"
        self.discussion = f"https://osu.ppy.sh/beatmapsets/{self.beatmapset_id}/discussion"
        self.preview_url = f"https://b.ppy.sh/preview/{self.beatmapset_id}.mp3"
        self.direct = f"osu://dl/{self.beatmapset_id}"
        beatmaps = []
        for beatmap in diffs:
            beatmaps.append(Beatmap(beatmap))
        self.beatmaps = beatmaps

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.creator})"
