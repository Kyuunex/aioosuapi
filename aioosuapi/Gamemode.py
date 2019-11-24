class Gamemode:
    def __init__(self, mode_id):
        gamemodes = [
            "osu!",
            "osu!taiko",
            "osu!catch",
            "osu!mania",
        ]
        if not mode_id:
            self.gamemode = ""
        else:
            self.gamemode = gamemodes[int(mode_id)]

    def __str__(self):
        return self.gamemode
