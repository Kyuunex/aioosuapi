import aiohttp
import html
import json


async def get_contents_in_between(after, before, string):
    return ((string.split(after))[1].split(before)[0]).strip()


class aioosuwebapi:
    # def __init__(self, token):
    #     self._token = token

    async def raw_request(self, endpoint_category, endpoint, query):
        base_url = "https://osu.ppy.sh/"
        url = base_url+endpoint_category+'/'+query+'/'+endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_text = (await response.text())
                if len(response_text) > 4:
                    return response_text
                else:
                    raise ValueError('Connection issues')

    async def discussion(self, beatmapset_id):
        http_contents = await self.raw_request('beatmapsets', 'discussion', beatmapset_id)
        if "json-beatmapset-discussion" in http_contents:
            results = await get_contents_in_between('<script id="json-beatmapset-discussion" type="application/json">', '</script>', http_contents)
            return json.loads(results)
        elif "<h1>Page Missing</h1>" in http_contents:
            return {
                "beatmapset": {
                    "status": "deleted"
                }
            }
        else:
            raise ValueError('Endpoint has most likely been changed')

    async def groups(self, group_id):
        http_contents = await self.raw_request('groups', '', group_id)
        if "json-users" in http_contents:
            result = await get_contents_in_between('<script id="json-users" type="application/json">', '</script>', http_contents)
            return json.loads(result)
        else:
            raise ValueError('Endpoint has most likely been changed')
