# 2023-09-08 (소요시간 : X 해설봐가면서 익히는중)
# 백트래킹 [실버2. 백준 10819 차이를 최대로] (https://www.acmicpc.net/problem/10819)

N = int(input())
data = list(map(int, input().split()))


max_data = -int(1e9)
arr = []

visit = [False] * (N)


def dfs():
    global max_data
    if len(arr) == N:
        sum_ = 0
        for i in range(N - 1):
            sum_ += abs(arr[i] - arr[i + 1])
        max_data = max(max_data, sum_)
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            arr.append(data[i])
            dfs()
            visit[i] = False
            arr.pop()


dfs()
print(max_data)
