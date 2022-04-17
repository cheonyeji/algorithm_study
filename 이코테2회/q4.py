# 2022-04-17
# 이코테 2회차 그리디 Q4 만들 수 없는 금액

"""
현재 상태에서 매번 좋은 것만 선택하기
현재 상태 : 1부터 target-1까지의 모든 금액을 만들 수 있는 상태
-> 매번 target 금액을 만들 수 있는지 체크 (=현재 확인하는 동전의 단위가 target 이하인지)
"""


n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1

for i in coins:
    if i <= target:
        target += i
    else:
        break

print(target)


"""
TC 1 -> 8
5
3 2 1 1 9

TC 2 -> 7
4
1 2 3 8 
"""
