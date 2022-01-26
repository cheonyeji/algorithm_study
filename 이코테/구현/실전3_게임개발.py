# 2021-01-26
# 이코테 ch4 구현 실전 문제 3 게임 개발

# n : 세로(열),  m : 가로(행)
n, m = map(int, input().split())

# d: 0, 1, 2, 3 -> 북, 동, 남, 서
x, y, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = [0, 1, 2, 3]

graph = [list(map(int, input().split())) for _ in range(m)]

# 현재 플레이어가 서있는 위치 방문처리
graph[x][y] = 2

count = 1

while 0 <= x <= n and 0 <= y <= m:
    moved = False

    for i in range(len(direction)):
        # 1. 왼쪽방향으로 회전
        n_dir = d - 1
        d = direction[n_dir]
        # 2. 그 방향에 가보지 않은 칸이 존재한다면 그 방향으로 한칸 전진
        nx = x + dx[n_dir]
        ny = y + dy[n_dir]
        if 0 <= nx <= n and 0 <= ny <= m and graph[nx][ny] != 1 and graph[nx][ny] != 2:
            graph[nx][ny] = 2  # 방문처리 : 2
            count += 1
            x, y = nx, ny
            moved = True
            break
        # 가보지 않은 칸이 없다면 회전만
        else:
            continue

    # 3. 네 방향 모두 이동 불가능인 경우, 원 방향을 유지한 채로 한칸 뒤로 가고 1단계로 반복
    if not moved:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤쪽방향이 바다가 아닌 경우에만 뒤로 한칸
        if 0 <= nx <= n and 0 <= ny <= m and graph[nx][ny] != 1:
            x, y = nx, ny
        else:
            # 움직임 멈춤
            break

print(count)

"""
TC -> 3
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
