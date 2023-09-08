# 2023-06-07
# 백준 - 백트래킹
# https://www.acmicpc.net/problem/9663
# 소요 시간 : 17:55 ~ 19:07 (70m)

# pypy3로만 통과됨 그냥 파이썬은 시간초과
from sys import stdin

input = stdin.readline

N = int(input())
row = [0] * N  # 인덱스번째 행에 y좌표에 퀸이 존재한다
result = 0


def isOk(x):
    # i 값 : 행. row[i] 값이 열
    for i in range(x):
        # 열이 같거나 대각선에 있으면 안됨 (대각선여부는 행-행 == 열-열)
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(node):
    global result
    if node == N:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N):
            row[node] = i
            if isOk(node):
                dfs(node + 1)


dfs(0)
print(result)

"""
바킹독님 풀이 뭔소리인지 잘 모르겠어서 기록만 해두고 다른 풀이로 이해함

isUsed1 = [False] * 15  # 열
isUsed2 = [False] * 30  # / 방향 대각선
isUsed3 = [False] * 30  # \ 방향 대각선

cnt = 0
N = int(input())

# cur번째 row에 퀸을 놓음
def func(cur):
    global cnt
    # N개를 놓는데 성공했다면 끝
    if cur == N:
        cnt += 1
        return

    for i in range(N):  # (cur, i)에 퀸을 놓음
        # 열, /방향, \방향에서 걸리는게 있으면 진행X
        if isUsed1[i] or isUsed2[cur + i] or isUsed3[cur - i + N - 1]:
            continue
        isUsed1[i] = True
        isUsed2[i + cur] = True
        isUsed3[cur - i + N - 1] = True
        func(cur + 1)
        isUsed1[i] = False
        isUsed2[i + cur] = False
        isUsed3[cur - i + N - 1] = False


func(0)
print(cnt)
"""
