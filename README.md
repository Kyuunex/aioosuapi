# aioosuapi

Asynchronous osu! api wrapper

# Installation: 

Type this in terminal: `pip3 install git+https://github.com/Kyuunex/aioosuapi.git@v1`  
You should also: `pip3 install aiohttp`


# Usage:
```python
from aioosuapi import aioosuapi

osu = aioosuapi.aioosuapi("your_osu_api_key")

# How to request something
result = await osu.method_name(parameters_go_here) 

print(result.something)

```
For example:
```python
result = await osu.get_user(u="1623405") 

print(result.name)
# Okoratu
```

What parameters you can pass can be found here: https://github.com/ppy/osu-api/wiki  
Use them on methods with the same name. `get_beatmapset` shares the same parameters as `get_beatmaps`.

# Methods:
1. `get_beatmaps` - Retrieve general beatmap information. Returns a **list** of `Beatmap` objects.
2. `get_beatmapset` - Retrieve a general information on a mapset. Returns a `Beatmapset` object. (WARNING: This is very experimental, only pass in `s` parameter. Do not pass in `u` parameter, this is gonna return a random beatmapset from this user with all diffs from all other sets. This is broken for now.)
3. `get_user` - Retrieve general user information. Returns a `User` object.
4. `get_scores` - Retrieve information about the top 100 scores of a specified beatmap. Returns a **list** of `BeatmapScore` objects.
5. `get_user_best` - Get the top scores for the specified user. Returns a **list** of `UserScore` objects.
6. `get_user_recent` - Gets the user's ten most recent plays over the last 24 hours. Returns a **list** of `UserRecentScore` objects.
7. `get_match` - Retrieve information about multiplayer match. Returns a `Match` object.
8. `get_replay` - Get the replay data of a user's score on a map. Heavy request, rate limited at 10 requests per minute. Returns `Replay` object.

# Objects:

### `User`:
```python
user_id # User account id
id # User account id
username # Username
name # Username
join_date # Join date in UTC
count300
count100
count50
playcount
ranked_score
total_score
pp_rank # Global rank
rank # Global rank
level
pp_raw # pp
pp # pp
accuracy
count_rank_ss
count_rank_ssh
count_rank_s
count_rank_sh
count_rank_a
country # ISO3166-1 alpha-2 code
total_seconds_played
country_rank # Country rank
avatar # User's avatar url
url # User's profile url
events # A list of UserEvent objects.
```


### `UserEvent`:
```python
display_html
display_text # Same as above but not in HTML
beatmap_id
beatmapset_id
date # in UTC
epicfactor # How "epic" this event is supposed to be
id # ID of the event
```

### `Beatmap`:
```python
approved # 4 = loved, 3 = qualified, 2 = approved, 1 = ranked, 0 = pending, -1 = WIP, -2 = graveyard
submit_date # date submitted, in UTC
approved_date # date ranked, in UTC
last_update # last update date, in UTC
artist
beatmap_id
id # beatmap_id
beatmapset_id
bpm
creator
author # creator
creator_id
difficultyrating # The amount of stars the map would have ingame and on the website
diff_aim
diff_speed
diff_size # Circle size value (CS)
cs # Circle size value (CS)
diff_overall # Overall difficulty (OD)
od # Overall difficulty (OD)
diff_approach # Approach Rate (AR)
ar # Approach Rate (AR)
diff_drain # Health drain (HP)
hp # Health drain (HP)
hit_length # seconds from first note to last note not including breaks
source
genre_id # 0 = any, 1 = unspecified, 2 = video game, 3 = anime, 4 = rock, 5 = pop, 6 = other, 7 = novelty, 9 = hip hop, 10 = electronic (note that there's no 8)
language_id # 0 = any, 1 = other, 2 = english, 3 = japanese, 4 = chinese, 5 = instrumental, 6 = korean, 7 = french, 8 = german, 9 = swedish, 10 = spanish, 11 = italian
title # song name
total_length # seconds from first note to last note including breaks
version # difficulty name
file_md5 # md5 hash of the beatmap
mode # game mode id
gamemode # game mode name
tags # Beatmap tags separated by spaces
favourite_count # Number of times the beatmap was favourited.
rating
playcount # Number of times the beatmap was played
passcount # Number of times the beatmap was passed, completed (the user didn't fail or retry)
count_normal
count_slider
count_spinner
max_combo # The maximum combo a user can reach playing this beatmap.
download_unavailable # If the download for this beatmap is unavailable (old map, etc.)
audio_unavailable # If the audio for this beatmap is unavailable (DMCA takedown, etc.)
thumbnail # low res background
cover # background but cropped, but higher resolution
url # beatmap url
```