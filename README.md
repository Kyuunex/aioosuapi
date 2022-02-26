# aioosuapi

An asynchronous osu! API wrapper

This branch is for Version 2 of the osu! API. 
Somewhat usable but not fully featured. For now, some stuff scrapes some pages.

### Installation: 

To install the latest commit, type this in terminal: 
`pip3 install git+https://github.com/Kyuunex/aioosuapi.git@v2`  
It's recommended to install a version from the releases section though.


# Quick example:
```python
from aioosuwebapi import aioosuwebapi

osuweb = aioosuwebapi("your_client_id", "your_client_secret")

result = await osuweb.get_user("1623405") 

print(result['username'])
# Okoratu
```
