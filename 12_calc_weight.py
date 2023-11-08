#!/usr/bin/python3
def calc_weight(list_=[]):
    if not list_:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in list_:
        total_score += score * weight
        total_weight += weight

    weighted_average = total_score / total_weight
    return weighted_average

if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")


