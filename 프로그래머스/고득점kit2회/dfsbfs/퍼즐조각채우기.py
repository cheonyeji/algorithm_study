# 2023-08-06 (2시간 걸려서 고생하다가 해설참고)

from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 시계방향 90도 회전
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res


# 전달받은 location 배열에서 좌측하단, 우측상단 좌표값 뽑아내는 코드 (사각형으로 가공)
def get_new_locations(location):
    new_locations = []
    for loc in location:
        x_min = int(1e9)
        x_max = 0
        y_min = int(1e9)
        y_max = 0
        for x, y in loc:
            x_min = min(x_min, x)
            x_max = max(x_max, x)
            y_min = min(y_min, y)
            y_max = max(y_max, y)
        new_locations.append([x_min, x_max, y_min, y_max])
    return new_locations


# table 돌면서 연결된 하나의 블록 좌표 모두 뽑아내는 BFS
def bfs(table, q, location, n):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if table[nx][ny] == 1:
                    location.append([nx, ny])
                    table[nx][ny] = 0  # 더이상 방문하지 않도록 0으로 처리
                    q.append([nx, ny])
    return location


def get_piece_or_space(table, new_locations):
    pieces = []  # 사각형 모양 저장할 배열
    for x_min, x_max, y_min, y_max in new_locations:
        piece = []  # 가로줄 한줄
        for x in range(x_min, x_max + 1):
            row = table[x]
            piece.append(row[y_min : y_max + 1])
        pieces.append(piece)
    return pieces


def solution(game_board, table):
    answer = 0

    n = len(table)

    # 비교를 편하게 하기 위해 game_board 좌표값 0 <-> 1 바꾸기 (table과 통일)
    for x in range(n):
        for y in range(n):
            if game_board[x][y] == 0:
                game_board[x][y] = 1
            else:
                game_board[x][y] = 0

    # 사각형 좌표 뽑아내야되서 원본을 건드리지 않도록 원본 table 배열 복제
    new_table = copy.deepcopy(table)

    # 퍼즐 뽑아내기
    puzzle = []
    for x in range(n):
        for y in range(n):
            if new_table[x][y] == 1:
                new_table[x][y] = 0
                q = deque([[x, y]])
                location = [[x, y]]
                puzzle.append(bfs(new_table, q, location, n))

    new_locations = get_new_locations(puzzle)
    pieces = get_piece_or_space(table, new_locations)

    # 4방향 회전
    for _ in range(4):
        new_pieces = []
        for piece in pieces:
            new_pieces.append(rotate_a_matrix_by_90_degree(piece))

        new_game_board = copy.deepcopy(game_board)  # 방문처리용으로 쓸 game_board 배열 복제

        for x in range(n):
            for y in range(n):
                if new_game_board[x][y] == 1:
                    new_game_board[x][y] = 0  # 방문 처리
                    q = deque([[x, y]])
                    location = [[x, y]]

                    # 빈 공간을 조각과 동일하게 사각형 형태로 가공하여 퍼즐조각과 같은지 비교
                    new_location = get_new_locations(
                        [bfs(new_game_board, q, location, n)]
                    )

                    space = get_piece_or_space(game_board, new_location)[0]
                    if space in new_pieces:
                        new_pieces.remove(space)  # 동일한 조각을 또 보면 안되니까 제거
                        for x_min, x_max, y_min, y_max in new_location:
                            for x in range(x_min, x_max + 1):
                                for y in range(y_min, y_max + 1):
                                    if game_board[x][y] == 1:
                                        game_board[x][y] = 0
                                        answer += 1
        pieces = new_pieces

    return answer
