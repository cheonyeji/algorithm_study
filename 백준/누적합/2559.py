# 2023-08-28 (소요시간 : 25m)
# 누적합 https://www.acmicpc.net/problem/2559

"""
최대, 최소 구할 때 int(1e9) 사용할것 (0 함부로 사용X)
온도의 누적합 배열을 만들어준 뒤, acc[i+K] - acc[i]가 가장 큰 경우 출력하기 
"""

from sys import stdin

input = stdin.readline

N, K = map(int, input().split(" "))
data = list(map(int, input().split(" ")))

acc = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if i == 1:
        acc[i] = data[i - 1]
        continue
    acc[i] = acc[i - 1] + data[i - 1]

result = -int(1e9)
for i in range(0, N - K + 1):
    result = max(result, acc[i + K] - acc[i])

print(result)
