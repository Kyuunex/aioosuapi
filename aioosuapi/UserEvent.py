import hashlib
from html import unescape
import re


class UserEvent:
    def __init__(self, dict):
        self.display_html = dict['display_html']
        self.display_text = unescape(re.sub('<[^<]+?>', '', self.display_html))
        self.beatmap_id = dict['beatmap_id']
        self.beatmapset_id = dict['beatmapset_id']
        self.date = dict['date']
        self.epicfactor = dict['epicfactor']
        self.id = hashlib.md5((self.date+self.beatmapset_id+self.beatmap_id+self.display_html).encode('utf-8')).hexdigest()

    def __str__(self):
        return self.display_text
