# 2022-04-17
# 이코테 2회차 그리디 Q5 볼링공 고르기

"""
(무게, 번호)로 배열을 만들고 무게 순 정렬하기로 풀까 했으나
무게별로 몇개의 공이 있는지만 체크해서 고려해도 충분해서 그렇게 했음
"""

n, m = map(int, input().split())

data = list(map(int, input().split()))

balls = [0] * (m + 1)

for i in data:
    balls[i] += 1

answer = 0

total = sum(balls)
for b in balls:
    if b == 0:
        continue
    answer += (b) * (total - b)
    total -= b

print(answer)

"""
TC 1 -> 8
5 3
1 3 2 3 2

TC 2 -> 25
8 5
1 5 4 3 2 4 5 2
"""
