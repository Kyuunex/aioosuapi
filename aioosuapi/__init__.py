"""
Asynchronous osu! api wrapper
"""


import aiohttp
import urllib

from .User import User
from .Beatmap import Beatmap
from .Beatmapset import Beatmapset
from .BeatmapScore import BeatmapScore
from .UserScore import UserScore
from .UserRecentScore import UserRecentScore
from .Match import Match
from .Replay import Replay


class aioosuapi:
    def __init__(self, token):
        self._token = token
        self._base_url = "https://osu.ppy.sh/api/"

    async def _raw_request(self, endpoint, parameters):
        parameters["k"] = self._token
        url = self._base_url+endpoint+"?"+urllib.parse.urlencode(parameters)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_json = await response.json()
                if "error" in response_json:
                    raise ValueError(response_json["error"])
                else:
                    return response_json

    async def _group_beatmaps_into_a_set(self, results):
        beatmapsets_dict = {}
        for beatmap in results:
            beatmapset_id = str(beatmap["beatmapset_id"])
            if not beatmapset_id in beatmapsets_dict:
                beatmapsets_dict[beatmapset_id] = []
            beatmapsets_dict[beatmapset_id].append(beatmap)
        beatmapsets = []
        for _, beatmapset in beatmapsets_dict.items():
            beatmapsets.append(beatmapset)
        return beatmapsets

    async def get_beatmaps(self, **kwargs):
        results = await self._raw_request("get_beatmaps", kwargs)
        if results:
            beatmaps = []
            for beatmap in results:
                beatmaps.append(Beatmap(beatmap))
            return beatmaps
        else:
            return []

    async def get_beatmap(self, **kwargs):
        results = await self._raw_request("get_beatmaps", kwargs)
        if results:
            return Beatmap(results[0])
        else:
            return None

    async def get_beatmapsets(self, **kwargs):
        results = await self._raw_request("get_beatmaps", kwargs)
        if results:
            beatmapsets = []
            for beatmapset in await self._group_beatmaps_into_a_set(results):
                beatmapsets.append(Beatmapset(beatmapset))
            return beatmapsets
        else:
            return []

    async def get_beatmapset(self, **kwargs):
        results = await self._raw_request("get_beatmaps", kwargs)
        if results:
            beatmapsets = await self._group_beatmaps_into_a_set(results)
            if beatmapsets:
                return Beatmapset(beatmapsets[0])
            else:
                return None
        else:
            return None

    async def get_user(self, **kwargs):
        results = await self._raw_request("get_user", kwargs)
        if results:
            return User(results[0])
        else:
            return None

    async def get_scores(self, **kwargs):
        results = await self._raw_request("get_scores", kwargs)
        if results:
            scores = []
            for score in results:
                scores.append(BeatmapScore(score))
            return scores
        else:
            return []

    async def get_user_best(self, **kwargs):
        results = await self._raw_request("get_user_best", kwargs)
        if results:
            scores = []
            for score in results:
                scores.append(UserScore(score))
            return scores
        else:
            return []

    async def get_user_recent(self, **kwargs):
        results = await self._raw_request("get_user_recent", kwargs)
        if results:
            scores = []
            for score in results:
                scores.append(UserRecentScore(score))
            return scores
        else:
            return []

    async def get_match(self, **kwargs):
        results = await self._raw_request("get_match", kwargs)
        if results:
            return Match(results)
        else:
            return None

    async def get_replay(self, **kwargs):
        results = await self._raw_request("get_replay", kwargs)
        if results:
            return Replay(results)
        else:
            return None
