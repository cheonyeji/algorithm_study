# 2023-08-24 (소요시간 : 1h)
# 누적합 https://www.acmicpc.net/problem/11660

from sys import stdin

input = stdin.readline

N, M = map(int, input().split(" "))

table = [list(map(int, input().split(" "))) for _ in range(N)]

pos_arr = [list(map(int, input().split(" "))) for _ in range(M)]

# 누적합 구하기
# 점화식을 원활하게 구하기 위해 i==0, j==0일때는 0으로 채운다
# 누적합 배열의 인덱스는 원본 배열보다 1씩 크다
acc = [[0 for _ in range(len(table[0]) + 1)] for _ in range(N + 1)]

# 누적합 배열 계산
for i in range(1, len(table) + 1):
    for j in range(1, len(table[0]) + 1):
        acc[i][j] = (
            acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + table[i - 1][j - 1]
        )


# 문제에서 요구하는 데이터 출력하기
# 범위 내 부분합을 구하기
for i, j, x, y in pos_arr:
    result = acc[x][y] - acc[i - 1][y] - acc[x][j - 1] + acc[i - 1][j - 1]
    print(result)
