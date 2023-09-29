# 2023-09-28 (소요시간 : 15m)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버2. https://www.acmicpc.net/problem/22233

"""
set으로 차집합 처리하면 시간초과남
dict으로 키값 조회해야함 -> 데이터가 많으므로 해싱!!
"""

from sys import stdin

input = stdin.readline

N, M = map(int, input().split(" "))

input_ = [input().rstrip() for _ in range(N)]
keywords = dict.fromkeys(input_, 1)

answer = []
for _ in range(M):
    input2_ = list(input().rstrip().split(","))
    written = dict.fromkeys(input2_, 1)

    for key in written:
        result = keywords.get(key, -1)
        if result != -1:
            del keywords[key]

    answer.append(len(keywords))

for v in answer:
    print(v)
