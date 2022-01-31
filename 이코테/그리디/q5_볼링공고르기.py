# 2021-01-31
# 이코테 ch11 그리디 문제 Q5 볼링공 고르기

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

i = 0
total = len(data)
answer = 0
while i < len(data):
    if data[i] == m:
        break
    same = data.count(data[i])
    for j in range(same):
        answer += total - same
        i += 1
    total -= same

print(answer)

"""
TC 1 -> 8
5 3
1 3 2 3 2
TC 2 -> 25
8 5
1 5 4 3 2 4 5 2
"""
