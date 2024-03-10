from collections import Counter


def solution(gems):
    answer = []
    dict_ = Counter(gems)

    start = 0
    end = len(gems) - 1

    start_fix = False
    end_fix = False
    temp_d = Counter(gems[start : end + 1])

    while not start_fix or not end_fix:
        if not end_fix:
            if len(temp_d) == len(dict_):
                if temp_d[gems[end]] == 1:
                    end_fix = True
                    continue
                temp_d[gems[end]] -= 1
                if temp_d[gems[end]] == 0:
                    del temp_d[gems[end]]
                end -= 1
                continue

        if not start_fix:
            if len(temp_d) == len(dict_):
                if temp_d[gems[start]] == 1:
                    start_fix = True
                    continue
                temp_d[gems[start]] -= 1
                if temp_d[gems[start]] == 0:
                    del temp_d[gems[start]]
                start += 1
                continue

    answer = [start + 1, end + 1]

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
