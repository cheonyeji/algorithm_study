# 2022-06-26
# 이코테 열흘동안 뽀개기 프로젝트 3일차
# 구현 실전 3 게임 개발
# 소요 시간 : 30분

n, m = map(int, input().split())

# 방문 위치 저장용 맵
vistied = [[0] * m for _ in range(n)]
row, col, direction = map(int, input().split())
vistied[row][col] = 1

# 전체 맵 정보
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 4방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 왼쪽 회전
def turnLeft():
    global direction
    direction -= 1
    # 북쪽에서 한번 더 왼쪽으로 돌면 서쪽을 보도록 설정
    if direction == -1:
        direction = 3


answer = 1
turn_cnt = 0  # 몇번 돌았는지 저장

while True:
    # 왼쪽 회전
    turnLeft()
    nr = row + dr[direction]
    nc = col + dc[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if vistied[nr][nc] == 0 and array[nr][nc] == 0:
        # 방문
        vistied[nr][nc] = 1
        # 이동했으니 좌표값 변경
        row = nr
        col = nc
        answer += 1
        # 회전 횟수 초기화
        turn_cnt = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나, 바다인 경우 회전 횟수 증가
    else:
        turn_cnt += 1

    # 네 방향을 모두 보았을 때 못 가는 경우
    if turn_cnt == 4:
        # 현재 방향 유지하고 한칸 뒤로
        nr = row - dr[direction]
        nc = col - dc[direction]

        # 뒤로 갈 수 있으면 이동
        if array[nr][nc] == 0:
            row = nr
            col = nc

        # 뒤가 바다로 막혀있는 경우
        else:
            # 이동 무한루프 탈출
            break

        # 다시 회전 횟수 초기화
        turn_cnt = 0


print(answer)

"""
TC -> 3
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
