class Scorer:
    def produce_scores(self, teams_data):
        scores = {}
        for tla in teams_data.keys():
            scores[tla] = 0
        return scores
