import aiohttp
import json
from bs4 import BeautifulSoup

from aioosuwebapi.exceptions import HTTPException
from aioosuwebapi.exceptions import OtherOsuAPIError


class aioosuwebscraper:
    def __init__(self):
        self._base_url = "https://osu.ppy.sh/"
        self._scrape_session = aiohttp.ClientSession()

    async def close(self):
        await self._scrape_session.close()

    async def scrape_latest_ranked_beatmapsets_array(self):
        async with self._scrape_session.get(self._base_url + "beatmapsets") as response:
            response_contents = await response.text()
            if len(response_contents) < 5:
                raise HTTPException("Connection issues")

        if not "json-beatmaps" in response_contents:
            raise OtherOsuAPIError("Endpoint has most likely been changed")

        soup = BeautifulSoup(response_contents, "html.parser")
        results = soup.find(id="json-beatmaps").string.strip()
        return json.loads(results)

    async def scrape_group_members_array(self, group_id):
        async with self._scrape_session.get(self._base_url + f"groups/{group_id}") as response:
            response_contents = await response.text()
            if len(response_contents) < 5:
                raise HTTPException("Connection issues")

        if not "json-users" in response_contents:
            raise OtherOsuAPIError("Endpoint has most likely been changed")

        soup = BeautifulSoup(response_contents, "html.parser")
        result = soup.find(id="json-users").string.strip()
        return json.loads(result)
