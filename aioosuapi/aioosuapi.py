"""
Asynchronous osu! api wrapper
Just pass in parameters from https://github.com/ppy/osu-api/wiki
"""


import aiohttp
import urllib

from .User import User
from .Beatmap import Beatmap
from .Beatmapset import Beatmapset
from .Score import Score
from .UserScore import UserScore
from .UserRecentScore import UserRecentScore
from .Match import Match
from .Replay import Replay


class aioosuapi:
    def __init__(self, token):
        self._token = token

    async def _raw_request(self, endpoint, parameters):
        parameters['k'] = self._token
        base_url = "https://osu.ppy.sh/api/"
        url = base_url+endpoint+'?'+urllib.parse.urlencode(parameters)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_json = await response.json()
                if "error" in response_json:
                    raise ValueError(response_json["error"])
                else:
                    return response_json

    async def get_beatmaps(self, **kwargs):
        results = await self._raw_request('get_beatmaps', kwargs)
        if results:
            beatmaps = []
            for beatmap in results:
                beatmaps.append(Beatmap(beatmap))
            return beatmaps
        else:
            return None

    async def get_beatmapset(self, **kwargs):
        results = await self._raw_request('get_beatmaps', kwargs)
        if results:
            return Beatmapset(results)
        else:
            return None

    async def get_user(self, **kwargs):
        results = await self._raw_request('get_user', kwargs)
        if results:
            return User(results[0])
        else:
            return None

    async def get_scores(self, **kwargs):
        results = await self._raw_request('get_scores', kwargs)
        if results:
            scores = []
            for score in results:
                scores.append(Score(score))
            return scores
        else:
            return None

    async def get_user_best(self, **kwargs):
        results = await self._raw_request('get_user_best', kwargs)
        if results:
            scores = []
            for score in results:
                scores.append(UserScore(score))
            return scores
        else:
            return None

    async def get_user_recent(self, **kwargs):
        results = await self._raw_request('get_user_recent', kwargs)
        if results:
            scores = []
            for score in results:
                scores.append(UserRecentScore(score))
            return scores
        else:
            return None

    async def get_match(self, **kwargs):
        results = await self._raw_request('get_match', kwargs)
        if results:
            return Match(results)
        else:
            return None

    async def get_replay(self, **kwargs):
        results = await self._raw_request('get_replay', kwargs)
        if results:
            return Replay(results)
        else:
            return None
