class ScoreParser:
    def __init__(self, loader):
        self.loader = loader

    def parse(self, value):
        return self.loader(value)
