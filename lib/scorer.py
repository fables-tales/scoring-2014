class Scorer:
    def produce_scores(parsed_scoresheet):
        for team in parsed_scoresheet.teams:
            Score(team)
