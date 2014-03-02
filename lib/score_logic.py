
def score_team(score_data):

    score = score_data['upright_tokens']

    if score_data['robot_moved']:
        score += 1

    score += len(set(score_data['zones_owned']))

    slots_owned = set(score_data['slots_owned'])
    score += len(slots_owned)

    # Plus the bonus for adjacent slots:
    for s in slots_owned:
        # 3 & 4 aren't next to each other as they're on opposite sides
        before = s - 1 if s != 4 else None
        after  = s + 1 if s != 3 else None

        if before in slots_owned or after in slots_owned:
            score += 1

    return score

def tidy_slots(slot_map):
    return slot_map

def tidy_zones(token_map):
    return token_map
