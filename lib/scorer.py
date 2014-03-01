class Scorer:
    def produce_scores(self, parsed_scoresheet):
        teams = parsed_scoresheet['teams']
        scores = {}
        for z, tla in enumerate(sorted(teams.keys())):
            scores[tla] = {
                "score": 0,
                "present": True,
                "disqualified": False,
                "zone": z,
            }
        return scores
