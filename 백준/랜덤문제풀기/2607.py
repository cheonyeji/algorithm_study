# 2023-09-28 (소요시간 : 15m)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버2. https://www.acmicpc.net/problem/2607

from collections import Counter
from sys import stdin

input = stdin.readline

K = int(input())

data = []
for _ in range(K):
    data.append(Counter(input().rstrip()))


def compare(c1, c2):
    diff = max(sum((c1 - c2).values()), sum((c2 - c1).values()))

    if diff <= 1:
        return True
    else:
        return False


answer = 0
for i in range(1, len(data)):
    if compare(data[0], data[i]):
        answer += 1

print(answer)
