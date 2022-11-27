"""
An asynchronous osu! API wrapper
"""

import aiohttp
import asyncio
from aiohttp import client_exceptions

from aioosuwebapi.exceptions import AuthenticationError
from aioosuwebapi.exceptions import HTTPException
from aioosuwebapi.exceptions import OtherOsuAPIError
from aioosuwebapi.exceptions import NotReady


class aioosuwebapi:
    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret

        self._base_url = "https://osu.ppy.sh/api/v2/"

        self._maintenance_session_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self._maintenance_session_payload = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "grant_type": "client_credentials",
            "scope": "public"
        }

        self._session = None
        self._maintenance_session = aiohttp.ClientSession(headers=self._maintenance_session_headers)

        self._loop = asyncio.get_event_loop()
        self._keepalive_task = self._loop.create_task(self._session_maintenance_loop())

    async def _session_maintenance_loop(self):
        while True:
            # TODO: Get a much better approach on this for the reasoning below.
            # Unsure about this double try blocks as cancellation could occur in
            # second try block or in the second except block.
            # As of now just wrap them in a try-except block to catch both events.
            try:
                async with self._maintenance_session.post("https://osu.ppy.sh/oauth/token",
                                                          json=self._maintenance_session_payload) as response:
                    response_json = await response.json()

                    if "error" in response_json:
                        if response_json["error"] == "unsupported_grant_type":
                            raise AuthenticationError(response_json["error_description"])
                        else:
                            raise OtherOsuAPIError(response_json["error"])

                    session_headers = {
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {response_json['access_token']}"
                    }
                    if self._session:
                        await self._session.close()
                    self._session = aiohttp.ClientSession(headers=session_headers)
                await asyncio.sleep(response_json["expires_in"])

            # Another side effect is that if cancellation occurs in try block, the Exception
            # block will also catch it and will only prints it, making the block endlessly loops.
            # To counter this, we just return the function.
            except asyncio.CancelledError:
                return
            except client_exceptions.ClientConnectorError as e:
                print(e)
                await asyncio.sleep(7200)

    # async def _error_handler(self, response):
    #     response_contents = await response.json()
    #     if 'error' in response_contents:
    #         raise OtherOsuAPIError(response_contents)

    async def close(self):
        self._keepalive_task.cancel()

        # If self._session_maintenance_loop fails for any reason, self._session will always be None.
        # This prevents trying to call .close() if the session isn't initiated yet as it doesn't
        # exist in NoneType, obviously.
        if self._session:
            await self._session.close()
        await self._maintenance_session.close()

    async def get_user_array(self, user_id, mode=None, **kwargs):
        """
        This endpoint returns the detail of specified user.
        :param user_id: user's id
        :param mode: (optional) fruits, mania, osu, taiko
        :return: A dictionary containing information about a user
        """

        endpoint = f"users/{user_id}"
        if mode:
            endpoint += f"/{mode}"

        while not self._session:
            await asyncio.sleep(0.5)

        async with self._session.get(self._base_url + endpoint, params=kwargs) as response:
            response_contents = await response.json()
            if 'error' in response_contents:
                raise OtherOsuAPIError(response_contents)
            return response_contents

    async def get_user_recent_activity_array(self, user_id, **kwargs):
        """
        Returns recent activity.
        :param user_id: user's id
        :return: User's recent activity.
        """

        while not self._session:
            await asyncio.sleep(0.5)

        async with self._session.get(self._base_url + f"users/{user_id}/recent_activity", params=kwargs) as response:
            response_contents = await response.json()
            if 'error' in response_contents:
                raise OtherOsuAPIError(response_contents)
            return response_contents

    async def get_user_beatmaps_array(self, user_id, beatmap_type, **kwargs):
        """
        Returns the beatmaps of specified user.
        :param user_id: user's id
        :param beatmap_type: favourite, graveyard, loved, most_played, ranked_and_approved, unranked
        :return: An array of beatmaps of specified user.
        """

        while not self._session:
            await asyncio.sleep(0.5)

        async with self._session.get(self._base_url + f"users/{user_id}/beatmapsets/{beatmap_type}",
                                     params=kwargs) as response:
            response_contents = await response.json()
            if 'error' in response_contents:
                raise OtherOsuAPIError(response_contents)
            return response_contents

    async def get_user_scores_array(self, user_id, score_type, **kwargs):
        while not self._session:
            await asyncio.sleep(0.5)

        endpoint = f"users/{user_id}/scores/{score_type}"
        async with self._session.get(self._base_url + endpoint, params=kwargs) as response:
            response_contents = await response.json()
            if 'error' in response_contents:
                raise OtherOsuAPIError(response_contents)
            return response_contents

    async def get_beatmapset_discussions_array(self, **kwargs):
        while not self._session:
            await asyncio.sleep(0.5)

        async with self._session.get(self._base_url + f"beatmapsets/discussions", params=kwargs) as response:
            response_contents = await response.json()
            if 'error' in response_contents:
                raise OtherOsuAPIError(response_contents)
            return response_contents

    async def get_beatmapset_discussions_posts_array(self, **kwargs):
        while not self._session:
            await asyncio.sleep(0.5)

        async with self._session.get(self._base_url + f"beatmapsets/discussions/posts", params=kwargs) as response:
            response_contents = await response.json()
            if 'error' in response_contents:
                raise OtherOsuAPIError(response_contents)
            return response_contents
