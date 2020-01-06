# aioosuapi

Asynchronous osu! api wrapper

Not ready for use. I'm just waiting for osu-web api to go public before I work on this.

### To install type this in terminal: 

`pip3 install git+https://github.com/Kyuunex/aioosuapi.git@v2`


# Quick example:
```python
from aioosuwebapi import aioosuwebapi

osuweb = aioosuwebapi("your_osu_api_key")

result = await osuweb.get_user("1623405") 

print(result['name'])
# Okoratu
```
