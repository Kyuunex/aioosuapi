import hashlib
import binascii
from html import unescape
import re


class UserEvent:
    def __init__(self, event):
        self.display_html = event["display_html"]
        self.display_text = unescape(re.sub("<[^<]+?>", "", self.display_html))
        self.beatmap_id = event["beatmap_id"]
        self.beatmapset_id = event["beatmapset_id"]
        self.date = event["date"]
        self.epicfactor = event["epicfactor"]
        self.epic_factor = event["epicfactor"]
        self.id_hex = hashlib.md5((self.date+self.display_html).encode("utf-8")).hexdigest()
        self.id = binascii.crc32((self.date+self.display_html).encode("utf-8"))

    def __str__(self):
        return self.display_text
