from sys import stdin

input = stdin.readline

N = int(input())
K = int(input())

data = list(map(int, input().split(" ")))


def soltion():
    global N, K
    if K >= N:
        print(0)
        return

    data.sort()

    # 간격이 제일 넓은 곳부터 집중국을 세워야 이득
    gap = []
    for i in range(1, N):
        gap.append(data[i] - data[i - 1])
    gap.sort()

    # K=2 -> 1군데에 집중국
    # K=3 -> 2군데에 집중국
    # 뒤에서부터 k-1개 빼주기
    print(sum(gap[: N - K]))


soltion()
