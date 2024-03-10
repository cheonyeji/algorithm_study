def search(r, c, board, letter, visited, set_):
    Row = len(board)
    Col = len(board[1])

    dir_ = [[0, 1], [1, 0], [1, 1]]
    temp = []
    for i in range(3):
        nr = r + dir_[i][0]
        nc = c + dir_[i][1]
        if 0 <= nr < Row and 0 <= nc < Col:
            if board[nr][nc] != letter:
                break
            else:
                temp.append([nr, nc])

    if len(temp) == 3:
        visited[r][c] = True
        for row, col in temp:
            set_.add((row, col))
            visited[row][col] = True
        for row, col in temp:
            search(row, col, board, letter, visited, set_)

    return set_


def solution(m, n, board):
    answer = 0
    b = [list(item) for item in board]

    while True:
        bomb = set([])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and b[r][c] != "-":
                    set_ = search(r, c, b, b[r][c], visited, set([(r, c)]))
                    if len(set_) > 1:
                        for row, col in set_:
                            bomb.add((row, col))

        if len(bomb) != 0:
            # 블록 삭제
            answer += len(bomb)
            for row, col in bomb:
                b[row][col] = "-"

            # 블록 당겨오기
            for i in range(m - 1):
                for j in range(n):
                    if b[i][j] != "-" and b[i + 1][j] == "-":
                        b[i + 1][j] = b[i][j]
                        b[i][j] = "-"
        else:
            break

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
