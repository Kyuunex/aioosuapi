from .Gamemode import Gamemode


class Beatmap:
    def __init__(self, beatmap):
        self.approved = beatmap["approved"]
        self.submit_date = beatmap["submit_date"]
        self.approved_date = beatmap["approved_date"]
        self.last_update = beatmap["last_update"]
        self.artist = beatmap["artist"]
        self.beatmap_id = beatmap["beatmap_id"]
        self.id = beatmap["beatmap_id"]
        self.beatmapset_id = beatmap["beatmapset_id"]
        self.bpm = beatmap["bpm"]
        self.creator = beatmap["creator"]
        self.author = beatmap["creator"]
        self.creator_id = beatmap["creator_id"]
        self.difficultyrating = beatmap["difficultyrating"]
        self.difficulty_rating = beatmap["difficultyrating"]
        self.diff_aim = beatmap["diff_aim"]
        self.diff_speed = beatmap["diff_speed"]
        self.diff_size = beatmap["diff_size"]
        self.cs = beatmap["diff_size"]
        self.diff_overall = beatmap["diff_overall"]
        self.od = beatmap["diff_overall"]
        self.diff_approach = beatmap["diff_approach"]
        self.ar = beatmap["diff_approach"]
        self.diff_drain = beatmap["diff_drain"]
        self.hp = beatmap["diff_drain"]
        self.hit_length = beatmap["hit_length"]
        self.source = beatmap["source"]
        self.genre_id = beatmap["genre_id"]
        self.language_id = beatmap["language_id"]
        self.title = beatmap["title"]
        self.total_length = beatmap["total_length"]
        self.version = beatmap["version"]
        self.file_md5 = beatmap["file_md5"]
        self.mode = beatmap["mode"]
        self.gamemode = Gamemode(beatmap["mode"])
        self.tags = beatmap["tags"]
        self.favourite_count = beatmap["favourite_count"]
        self.rating = beatmap["rating"]
        self.playcount = beatmap["playcount"]
        self.play_count = beatmap["playcount"]
        self.passcount = beatmap["passcount"]
        self.pass_count = beatmap["passcount"]
        self.count_normal = beatmap["count_normal"]
        self.count_slider = beatmap["count_slider"]
        self.count_spinner = beatmap["count_spinner"]
        self.max_combo = beatmap["max_combo"]
        self.download_unavailable = beatmap["download_unavailable"]
        self.audio_unavailable = beatmap["audio_unavailable"]
        self.thumbnail = f"https://b.ppy.sh/thumb/{self.beatmapset_id}l.jpg"
        self.thumb = f"https://assets.ppy.sh/beatmaps/{self.beatmapset_id}/covers/list@2x.jpg"
        self.cover = f"https://assets.ppy.sh/beatmaps/{self.beatmapset_id}/covers/cover.jpg"
        self.url = f"https://osu.ppy.sh/beatmaps/{self.beatmap_id}"
        self.discussion = f"https://osu.ppy.sh/beatmapsets/{self.beatmapset_id}/discussion/{self.beatmap_id}/"
        self.preview_url = f"https://b.ppy.sh/preview/{self.beatmapset_id}.mp3"

    def __str__(self):
        return f"{self.artist} - {self.title} [{self.version}]"
