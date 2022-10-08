# 2022-10-07
# week1. 수학
# https://www.acmicpc.net/problem/15649
# 소요시간 : 19:02 ~ 19:24 (20m)

# 순열로 풀면 쉽고,, 백트래킹으로 풀어야 정석 방법쓰 ,,,,

# 순열 풀이
from itertools import permutations

n, m = map(int, input().split())

data = [i for i in range(1, n + 1)]

nPm = permutations(data, m)

for case in nPm:
    for i in range(len(case)):
        print(case[i], end="")
        if i != len(case) - 1:
            print(" ", end="")
    print()

# 백트래킹 풀이
n, m = map(int, input().split())
result = []


def backTracking():
    # 수열의 길이가 m이면 출력해주고 전단계로 돌아가기 (재귀 탈출)
    if len(result) == m:
        print(" ".join(map(str, result)))  # "구분자".join(리스트)
        return
    # 1 ~ n 까지 체크
    for i in range(1, n + 1):
        # 중복 체크
        if i not in result:
            result.append(i)
            backTracking()
            # return 문으로 돌아온 경우 실행되는 부분
            result.pop()  # n=4, m=3일때 1,2,3이 들어온 경우 3을 없앰으로써 전단계로 돌아감


backTracking()
