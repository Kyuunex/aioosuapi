"""
Asynchronous osu! api wrapper
"""

import aiohttp
import html
import json

class aioosuwebapi:
    def __init__(self, token):
        self._token = token
        self._base_url = "https://osu.ppy.sh/api/v2/"
        self._headers = {
            "Authorization": "Bearer %s" % (self._token),
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    async def _raw_request(self, endpoint):
        async with aiohttp.ClientSession(headers=self._headers) as session:
            async with session.get(self._base_url+endpoint) as response:
                response_json = (await response.json())
                return response_json

    async def get_beatmapset_discussions(self, beatmapset_id):
        return await self._raw_request('beatmapsets/%s/discussion' % (beatmapset_id))

    async def get_group_members(self, group_id):
        return await self._raw_request('groups/%s' % (group_id))

    async def get_user(self, user_id):
        return await self._raw_request("users/%s" % (user_id))

    async def get_my_friends(self):
        return await self._raw_request("friends")

    async def get_channel_list(self):
        return await self._raw_request("chat/channels")
