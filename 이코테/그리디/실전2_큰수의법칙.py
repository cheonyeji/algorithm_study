# 2021-01-30
# 이코테 ch3 그리디 실전 문제 2 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

sorted_data = sorted(data, reverse=True)

answer = 0
i = 0
while i < m:
    for j in range(k):
        answer += sorted_data[0]
        i += 1
    answer += sorted_data[1]
    i += 1

print(answer)
"""
TC -> 46
5 8 3
2 4 5 4 6
"""
