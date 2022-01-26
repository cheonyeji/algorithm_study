# 2021-01-26
# 이코테 ch4 구현 예제 4-1 상하좌우

n = int(input())
data = list(input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_dir = ["L", "R", "U", "D"]  # 좌 우 상 하

x, y = 1, 1


for i in data:
    for j in range(len(move_dir)):
        if i == move_dir[j]:
            if 1 <= x + dx[j] <= n and 1 <= y + dy[j] <= n:
                x += dx[j]
                y += dy[j]
            break

print(x, y)

"""
TC -> 3 4 
5
R R R U D D
"""
