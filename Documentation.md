# Documentation

### Usage:
```python
from aioosuapi import aioosuapi

osu = aioosuapi("your_osu_api_key")

# How to request something
result = await osu.method_name(parameters_go_here) 

print(result.something)

```

What parameters you can pass can be found here: https://github.com/ppy/osu-api/wiki  
Use them on methods with the same name. `get_beatmapset` and `get_beatmapsets` share the same parameters as `get_beatmaps`.

# Methods:
+ `get_beatmaps` - Retrieve general beatmap information. Returns a **list** of `Beatmap` objects.
+ `get_beatmapsets` - Retrieve a general information on a beatmapset. Returns a **list** of `Beatmapset` objects.
+ `get_beatmapset` - Retrieve a general information on a beatmapset. Returns a `Beatmapset` object.
+ `get_user` - Retrieve general user information. Returns a `User` object.
+ `get_scores` - Retrieve information about the top 100 scores of a specified beatmap. Returns a **list** of `BeatmapScore` objects.
+ `get_user_best` - Get the top scores for the specified user. Returns a **list** of `UserScore` objects.
+ `get_user_recent` - Gets the user's ten most recent plays over the last 24 hours. Returns a **list** of `UserRecentScore` objects.
+ `get_match` - Retrieve information about multiplayer match. Returns a `Match` object.
+ `get_replay` - Get the replay data of a user's score on a map. Heavy request, rate limited at 10 requests per minute. Returns `Replay` object.

# Objects:

### `User`:
+ `user_id` - User account id
+ `id` - User account id
+ `username` - Username
+ `name` - Username
+ `join_date` - Join date in UTC
+ `count300`
+ `count100`
+ `count50`
+ `playcount`
+ `play_count`
+ `ranked_score`
+ `total_score`
+ `pp_rank` - Global rank
+ `rank` - Global rank
+ `level`
+ `pp_raw` - pp
+ `pp` - pp
+ `accuracy`
+ `count_rank_ss`
+ `count_rank_ssh`
+ `count_rank_s`
+ `count_rank_sh`
+ `count_rank_a`
+ `country` - ISO3166-1 alpha-2 code
+ `total_seconds_played`
+ `country_rank` - Country rank
+ `avatar` - User's avatar url
+ `url` - User's profile url
+ `events` - A list of UserEvent objects.


### `UserEvent`:
+ `display_html`
+ `display_text` - Same as above but not in HTML
+ `beatmap_id`
+ `beatmapset_id`
+ `date` - in UTC
+ `epicfactor` - How "epic" this event is supposed to be
+ `epic_factor` - Same as above
+ `id` - ID of the event

### `Beatmap`:
+ `approved` - 4 = loved, 3 = qualified, 2 = approved, 1 = ranked, 0 = pending, -1 = WIP, -2 = graveyard
+ `submit_date` - date submitted, in UTC
+ `approved_date` - date ranked, in UTC
+ `last_update` - last update date, in UTC
+ `artist`
+ `beatmap_id`
+ `id` - beatmap_id
+ `beatmapset_id`
+ `bpm`
+ `creator`
+ `creator_id`
+ `difficultyrating` - The amount of stars the map would have ingame and on the website
+ `difficulty_rating` - Same as above
+ `diff_aim`
+ `diff_speed`
+ `diff_size` - Circle size value (CS)
+ `cs` - Circle size value (CS)
+ `diff_overall` - Overall difficulty (OD)
+ `od` - Overall difficulty (OD)
+ `diff_approach` - Approach Rate (AR)
+ `ar` - Approach Rate (AR)
+ `diff_drain` - Health drain (HP)
+ `hp` - Health drain (HP)
+ `hit_length` - seconds from first note to last note not including breaks
+ `source`
+ `genre_id` - 0 = any, 1 = unspecified, 2 = video game, 3 = anime, 4 = rock, 5 = pop, 6 = other, 7 = novelty, 9 = hip hop, 10 = electronic (note that there's no 8)
+ `language_id` - 0 = any, 1 = other, 2 = english, 3 = japanese, 4 = chinese, 5 = instrumental, 6 = korean, 7 = french, 8 = german, 9 = swedish, 10 = spanish, 11 = italian
+ `title` - song name
+ `total_length` - seconds from first note to last note including breaks
+ `version` - difficulty name
+ `file_md5` - md5 hash of the beatmap
+ `mode` - game mode id
+ `gamemode` - game mode name
+ `tags` - Beatmap tags separated by spaces
+ `favourite_count` - Number of times the beatmap was favourited.
+ `rating`
+ `playcount` - Number of times the beatmap was played
+ `play_count` - Same as above
+ `passcount` - Number of times the beatmap was passed, completed (the user didn't fail or retry)
+ `pass_count` - Same as above
+ `count_normal`
+ `count_slider`
+ `count_spinner`
+ `max_combo` - The maximum combo a user can reach playing this beatmap.
+ `storyboard` - If this beatmap has a storyboard
+ `video` - If this beatmap has a video
+ `download_unavailable` - If the download for this beatmap is unavailable (old map, etc.)
+ `audio_unavailable` - If the audio for this beatmap is unavailable (DMCA takedown, etc.)
+ `thumbnail` - thumbnail old website
+ `thumb` - thumbnail new website
+ `cover` - cover new website
+ `url` - url
+ `discussion` - moddingv2
+ `preview_url` - preview mp3 url

### `Beatmapset`:
+ `approved` - 4 = loved, 3 = qualified, 2 = approved, 1 = ranked, 0 = pending, -1 = WIP, -2 = graveyard
+ `submit_date` - date submitted, in UTC
+ `approved_date` - date ranked, in UTC
+ `last_update` - last update date, in UTC
+ `artist`
+ `id` - beatmap_id
+ `beatmapset_id`
+ `bpm`
+ `creator`
+ `creator_id`
+ `source`
+ `genre_id` - 0 = any, 1 = unspecified, 2 = video game, 3 = anime, 4 = rock, 5 = pop, 6 = other, 7 = novelty, 9 = hip hop, 10 = electronic (note that there's no 8)
+ `language_id` - 0 = any, 1 = other, 2 = english, 3 = japanese, 4 = chinese, 5 = instrumental, 6 = korean, 7 = french, 8 = german, 9 = swedish, 10 = spanish, 11 = italian
+ `title`
+ `total_length` - seconds from first note to last note including breaks
+ `tags` - Beatmap tags separated by spaces
+ `favourite_count` - Number of times the beatmap was favourited.
+ `rating` 
+ `download_unavailable` - If the download for this beatmap is unavailable (old map, etc.)
+ `audio_unavailable` - If the audio for this beatmap is unavailable (DMCA takedown, etc.)
+ `thumbnail` - thumbnail old website
+ `thumb` - thumbnail new website
+ `cover` - cover new website
+ `url` - Beatmapset url
+ `discussion` - modding v2 page
+ `preview_url` - preview mp3 url
+ `direct` - osu!direct url
+ `beatmaps` - difficulties. a list of `Beatmap` objects
