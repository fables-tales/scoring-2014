
class Scorer:
    def __init__(self, scoresheet):
        self._scoresheet = scoresheet

    def calculate_scores(self):
        scores = {}
        for tla in self._scoresheet.keys():
            scores[tla] = 0
        return scores
