# aioosuapi

Asynchronous osu! api wrapper

# Installation: 

Type this in terminal: `pip3 install git+https://github.com/Kyuunex/aioosuapi.git@v1`  


# Quick example:
```python
from aioosuapi import aioosuapi

osu = aioosuapi("your_osu_api_key")

result = await osu.get_user(u="1623405") 

print(result.name)
# Okoratu
```

See `Documentation.md` for documentation.
