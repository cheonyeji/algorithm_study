# 2023-09-08 (소요시간 : X 해설봄)
# 백트래킹 [실버3. 백준 10974 모든 순열] (https://www.acmicpc.net/problem/10974)


from sys import stdin

input = stdin.readline

N = int(input())

arr = []


def dfs():
    if len(arr) == N:
        print(" ".join(map(str, arr)))
        # print(*arr) 해줘도 됨
        return
    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()


dfs()
