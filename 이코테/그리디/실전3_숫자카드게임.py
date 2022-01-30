# 2021-01-30
# 이코테 ch3 그리디 실전 문제 3 숫자 카드 게임

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

answer = -1

# 가장 큰 min_val 찾기
for i in range(len(data)):
    data[i].sort()
    answer = max(answer, data[i][0])

print(answer)

"""
TC 1 -> 2
3 3
3 1 2
4 1 4
2 2 2
TC 2 -> 3
2 4
7 3 1 8
3 3 3 4
"""
