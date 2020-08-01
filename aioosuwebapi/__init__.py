"""
Asynchronous osu! api wrapper
"""

import aiohttp
import asyncio


class aioosuwebapi:
    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token = ""
        self._base_url = "https://osu.ppy.sh/api/v2/"
        self._headers = {
            "Authorization": f"Bearer {self._token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        loop = asyncio.get_event_loop()
        loop.create_task(self.token_guarantee_service_loop())
        # loop.run_until_complete(self.make_client_session())

    async def token_guarantee_service_loop(self):
        while True:
            try:
                payload = {
                    "client_id": self._client_id,
                    "client_secret": self._client_secret,
                    "grant_type": "client_credentials",
                    "scope": "public"
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post("https://osu.ppy.sh/oauth/token", data=payload) as response:
                        response_json = await response.json()
                        self._token = response_json["access_token"]
                await asyncio.sleep(response_json["expires_in"])
            except Exception as e:
                print(e)
                await asyncio.sleep(7200)

    async def _raw_request(self, endpoint):
        async with aiohttp.ClientSession(headers=self._headers) as session:
            async with session.get(self._base_url+endpoint) as response:
                response_json = (await response.json())
                return response_json

    async def get_beatmapset_discussions(self, beatmapset_id):
        return await self._raw_request(f"beatmapsets/{beatmapset_id}/discussion")

    async def get_group_members(self, group_id):
        return await self._raw_request(f"groups/{group_id}")

    async def get_user(self, user_id):
        return await self._raw_request(f"users/{user_id}")

    async def get_my_friends(self):
        return await self._raw_request("friends")

    async def get_channel_list(self):
        return await self._raw_request("chat/channels")
