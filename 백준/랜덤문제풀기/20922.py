# 2023-09-28 (소요시간 : 40m+해설참고)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버1. https://www.acmicpc.net/problem/20922

"""
모든 부분수열을 다 보면 무조건 시간초과
start, end로 접근해야되는것까지는 잘 잡았는데
왼쪽으로 이동하면서 딕셔너리에서 빼주는걸 이해를 못했음
start, end는 인덱스니까 data[start], data[end]로 접근해서
등장횟수 count해주는 딕셔너리를 업데이트해주면 됨

end가 끝까지 가면 그만 볼것
"""

from sys import stdin
from collections import defaultdict

input = stdin.readline

N, K = map(int, input().split(" "))
data = list(map(int, input().split(" ")))

max_length = -int(1e9)

dict_ = defaultdict(int)
start = 0
end = 0

while True:
    if end == N:
        break
    if dict_[data[end]] < K:
        dict_[data[end]] += 1
        end += 1
    else:
        dict_[data[start]] -= 1
        start += 1

    max_length = max(end - start, max_length)


print(max_length)
