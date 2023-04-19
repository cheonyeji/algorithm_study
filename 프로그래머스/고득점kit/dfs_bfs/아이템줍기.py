# 2023-04-19
# 프로그래머스 고득점 kit - DFS/BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 소요 시간 : 못 풀어서 해설 참고... 나중에 한번 더 츄라이

"""
테두리만 1로 남겨서 bfs할수있는 그래프를 만들어주면 되는 문제였음
다만 그냥 하게 되면 인접한 요소에서 테두리로 가지 않고 직선으로 가버림
ex. 아래와 같은 그림에서 바깥쪽으로 안가고 안쪽으로 먼저 가버림
1 1
1 1
0 1 
이 상황 해결을 위해 인접한 요소를 아예 없애기 위해 좌표를 x2해서 처리해준 뒤
정답만 //2해서 리턴해줘야 함

bfs를 도는 아이디어 자체는 똑같은데 그래프를 어떻게 생성할 수 있을지를 더 고민해보게 된 문제

"""

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102
    graph = [[2] * MAX for _ in range(MAX)]  # 빈공간 : 2

    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda data: data * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:  # 내부
                    graph[i][j] = 0
                elif graph[i][j] != 0:  # 테두리 (여기서 else로 처리하면 안됨)
                    graph[i][j] = 1
    # 길찾기
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visit = [[0] * MAX for _ in range(MAX)]
    visit[characterX * 2][characterY * 2] = 1
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = (visit[x][y] - 1) // 2  # 좌표 2배로 처리해줬으므로 나눠줄것
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append([nx, ny])
                visit[nx][ny] = visit[x][y] + 1
    return answer
