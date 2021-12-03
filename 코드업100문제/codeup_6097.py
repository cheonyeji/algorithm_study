# 코드업 파이썬기초100제 - 6097 설탕과자뽑기
h, w = map(int, input().split())
board = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    if d:  # True=vertical
        for j in range(x, x + l):
            board[j][y] = 1
    else:
        for j in range(y, y + l):
            board[x][j] = 1

# 가로 세로가 매일 헷갈리는 이유는 뭘까
for i in range(h):
    for j in range(w):
        print(board[i][j], end=" ")
    print()
