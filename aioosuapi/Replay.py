class Replay:
    def __init__(self, dict):
        self.content = dict['content']
        self.encoding = dict['encoding']

    def __str__(self):
        return self.content
