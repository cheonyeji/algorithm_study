# 2023-09-28 (소요시간 : 20m)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버1. https://www.acmicpc.net/problem/2531

from sys import stdin
from collections import defaultdict

input = stdin.readline

N, d, k, c = map(int, input().split(" "))
data = [int(input().rstrip()) for _ in range(N)]

answer = 0
start = 0
end = start + k - 1

dict_ = defaultdict(int)
for i in range(start, end + 1):
    dict_[data[i]] += 1

while start < N:
    if c not in dict_:
        answer = max(len(dict_) + 1, answer)
    else:
        answer = max(len(dict_), answer)

    end += 1
    if end == N:
        end = 0
    dict_[data[end]] += 1
    dict_[data[start]] -= 1
    # 0이 되면 그 경우는 빼버리기
    if dict_[data[start]] == 0:
        del dict_[data[start]]
    start += 1

print(answer)
