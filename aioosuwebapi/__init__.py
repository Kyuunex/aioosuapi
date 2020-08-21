"""
Asynchronous osu! api wrapper
"""

import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup


class aioosuwebapi:
    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret

        self._base_url = "https://osu.ppy.sh/api/v2/"
        self._base_url2 = "https://osu.ppy.sh/"

        self._session = None
        self._session2 = aiohttp.ClientSession()

        self._loop = asyncio.get_event_loop()
        self._keepalive_task = self._loop.create_task(self._session_maintenance_loop())

    async def _session_maintenance_loop(self):
        while True:
            # TODO: Get a much better approach on this for the reasoning below.
            # Unsure about this double try blocks as cancellation could occur in
            # second try block or in the second except block.
            # As of now just wrap them in a try-except block to catch both events.
            try:
                try:
                    payload = {
                        "client_id": self._client_id,
                        "client_secret": self._client_secret,
                        "grant_type": "client_credentials",
                        "scope": "public"
                    }
                    async with self._session2.post("https://osu.ppy.sh/oauth/token", data=payload) as response:
                        response_json = await response.json()
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
                except Exception as e:
                    print(e)
                    await asyncio.sleep(7200)
            except asyncio.CancelledError:
                return

    async def _error_handler(self, response):
        response_contents = await response.json()
        if 'error' in response_contents:
            raise ValueError(response_contents['error'])

    async def close(self):
        self._keepalive_task.cancel()

        # If self._session_maintenance_loop fails for any reason, self._session will always be None.
        # This prevents trying to call .close() if the session isn't initiated yet as it doesn't
        # exist in NoneType, obviously.
        if self._session:
            await self._session.close()
        await self._session2.close()

    async def get_user_array(self, user_id):
        async with self._session.get(self._base_url + f"users/{user_id}") as response:
            await self._error_handler(response)
            return await response.json()

    async def scrape_beatmapset_discussions_array(self, beatmapset_id):
        async with self._session2.get(self._base_url2 + f"beatmapsets/{beatmapset_id}/discussion") as response:
            response_contents = await response.text()
            if len(response_contents) < 5:
                raise ValueError("Connection issues")

        if "json-beatmapset-discussion" in response_contents:
            soup = BeautifulSoup(response_contents, "html.parser")
            results = soup.find(id="json-beatmapset-discussion").string.strip()
            return json.loads(results)
        elif "<h1>Page Missing</h1>" in response_contents:
            # TODO: this should also raise a ValueError
            # what im doing is very retarded
            return {
                "beatmapset": {
                    "status": "deleted"
                }
            }
        else:
            raise ValueError("Endpoint has most likely been changed")

    async def scrape_latest_ranked_beatmapsets_array(self):
        async with self._session2.get(self._base_url2 + "beatmapsets") as response:
            response_contents = await response.text()
            if len(response_contents) < 5:
                raise ValueError("Connection issues")

        if not "json-beatmaps" in response_contents:
            raise ValueError("Endpoint has most likely been changed")

        soup = BeautifulSoup(response_contents, "html.parser")
        results = soup.find(id="json-beatmaps").string.strip()
        return json.loads(results)

    async def scrape_group_members_array(self, group_id):
        async with self._session2.get(self._base_url2 + f"groups/{group_id}") as response:
            response_contents = await response.text()
            if len(response_contents) < 5:
                raise ValueError("Connection issues")

        if not "json-users" in response_contents:
            raise ValueError("Endpoint has most likely been changed")

        soup = BeautifulSoup(response_contents, "html.parser")
        result = soup.find(id="json-users").string.strip()
        return json.loads(result)
