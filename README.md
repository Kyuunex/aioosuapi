# aioosuapi

An asynchronous osu! API wrapper

# Installation: 

To install the latest commit, type this in terminal: 
`pip3 install git+https://github.com/Kyuunex/aioosuapi.git@v1`  
It's recommended to install a version from the releases section though.

# Quick example:
```python
from aioosuapi import aioosuapi

osu = aioosuapi("your_osu_api_key")

result = await osu.get_user(u="1623405") 

print(result.name)
# Okoratu
```

See `Documentation.md` for documentation.
