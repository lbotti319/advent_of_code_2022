def make_score_map(letters: str):
    val =0
    score_map = {}
    for c in letters:
        score_map[c.upper()] = val
        val += 1
    return score_map
def make_reverse_map(letters: str):
    val = 0
    score_map = {}
    for c in letters:
        score_map[val] = c.upper()
        val += 1
    return score_map

def game(p1, p2):
    """
    1, 0, -1 for p1 win, draw, p2 win
    """
    if p1 == p2:
        return 0
    if (p1 + 1) % 3 == p2:
        return -1
    return 1

def part_one():
    score = 0
    shape_score = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    p1_scores = make_score_map("abc")
    p2_scores = make_score_map("xyz")
    with open("p2.input") as f:
        for line in f.readlines():
            p1, p2 = line.strip().split(" ")
            result = game(p1_scores[p1], p2_scores[p2])
            if result == 0:
                score += 3
            elif result == -1:
                score += 6
            score += shape_score[p2]
    return score

def get_counter(p1, result, score_map, reverse_map):
    if result == "X":
        return reverse_map[(score_map[p1] - 1) %3]
    elif result == "Y":
        return p1

    return reverse_map[(score_map[p1] + 1) %3]

def part_two():
    score = 0
    shape_score = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    p1_scores = make_score_map("abc")
    p2_scores = make_score_map("abc")
    reverse_map = make_reverse_map("abc")
    with open("p2.input") as f:
        for line in f.readlines():
            p1, result = line.strip().split(" ")
            p2 = get_counter(p1, result, p1_scores, reverse_map)
            result = game(p1_scores[p1], p2_scores[p2])
            if result == 0:
                score += 3
            elif result == -1:
                score += 6
            score += shape_score[p2]
    return score
print(part_one())
print(part_two())

