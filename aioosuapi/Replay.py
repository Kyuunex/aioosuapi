class Replay:
    def __init__(self, replay):
        self.content = replay["content"]
        self.encoding = replay["encoding"]

    def __str__(self):
        return self.content
