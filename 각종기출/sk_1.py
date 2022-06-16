# 2022-03-12
# SK Famliy FE/App 1차 코딩테스트 1번


def cmpCoin(c1, c2, costs):
    coins = [1, 5, 10, 50, 100, 500]

    if costs[c1] * (coins[c2] // coins[c1]) < costs[c2]:
        return c1
    else:
        return c2


def selectCoin(costs):
    result = [-1] * 6

    result[0] = 0  # 1원은 1원동전쓰기
    result[1] = cmpCoin(0, 1, costs)  # 1원5개, 5원1개 중에 고르기

    for i in range(2, 6):
        result[i] = cmpCoin(result[i - 1], i, costs)

    return result


def solution(money, costs):
    answer = 0
    result = selectCoin(costs)

    coins = [1, 5, 10, 50, 100, 500]

    for c in range(len(costs)):
        m = money // coins[len(costs) - 1 - c]
        need = coins[len(costs) - 1 - c] // coins[result[len(costs) - 1 - c]]
        answer += m * need * costs[result[len(costs) - 1 - c]]
        money -= m * coins[len(costs) - 1 - c]
    return answer


print(solution(4578, [1, 4, 99, 35, 50, 1000]))
