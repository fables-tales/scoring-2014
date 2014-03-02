
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
    owners = {}
    tidied = {}

    for tla, slots in slot_map.items():
        for s, val in slots.items():
            if val:
                if s in owners:
                    msg = "Slot {0} claims to be owned by at least '{1}' and '{2}'." \
                            .format(s, tla, owners[s])
                    raise Exception(msg)

                owners[s] = tla

        tidied[tla] = set()

    for slot, owner in owners.items():
        tidied[owner].add(slot)

    return tidied

def tidy_zones(token_map):
    return token_map
