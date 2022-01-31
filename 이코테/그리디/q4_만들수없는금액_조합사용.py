# 2021-01-31
# 이코테 ch11 그리디 문제 Q4 만들 수 없는 금액
# 내가 푼 방식 (극단적인 경우에는 시간초과가 날 수 있음)

from itertools import combinations


n = int(input())

coins = list(map(int, input().split()))
coins.sort()

money = 1

while True:
    if money in coins:
        money += 1
    elif money < coins[0]:
        break
    else:
        # money보다 더 작은 화폐단위끼리 지지고볶고 해서 체크
        max_range = 0
        for i in range(len(coins)):
            if coins[i] > money:
                max_range = i

        available = False
        for i in range(2, max_range + 1):
            if available:
                break
            for case in list(combinations(coins[:max_range], i)):
                if money == sum(case):
                    available = True
                    break

        # 지지고볶아서 못만듦
        if not available:
            break
        else:
            money += 1


print(money)

"""
TC -> 8
5
3 2 1 1 9
"""
