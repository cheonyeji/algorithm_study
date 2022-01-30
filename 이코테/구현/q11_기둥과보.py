# 2021-01-30
# 이코테 ch12 구현 문제 Q11 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

# 해설
# 구현 과정이 복잡하고, 시간이 5초로 넉넉하기 때문에 m^3의 시간복잡도로 간단하게 해결하는 풀이
# 설치 및 삭제 연산을 요구할때마다 일일히 전체 구조물을 확인하며 규칙 체크

# 현재 설치된 구조물이 가능한 구조물인지 확인
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥 설치
            if (
                y == 0
                or [x - 1, y, 1] in answer
                or [x, y, 1] in answer
                or [x, y - 1, 0] in answer
            ):
                continue
            return False
        elif stuff == 1:  # 보 설치
            if (
                [x, y - 1, 0] in answer
                or [x + 1, y - 1, 0] in answer
                or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)
            ):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)


print(
    solution(
        5,
        [
            [0, 0, 0, 1],
            [2, 0, 0, 1],
            [4, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [2, 1, 1, 1],
            [3, 1, 1, 1],
            [2, 0, 0, 0],
            [1, 1, 1, 0],
            [2, 2, 0, 1],
        ],
    )
)

# 테스트케이스 2개만 맞고 나머지 경우는 모두 틀린 판정이 난 풀이
# 기둥이 설치된 경우 해당 교차점의 왼쪽좌표에 +1
# 보가 설치된 경우 해당 교차점의 한칸 아래에 +2
"""
arr_g = []
arr_b = []

# 기둥이 조건 만족하는지 체크
def check_g(graph, x, y):
    # 바닥 위/ 보의 한쪽 끝 부분 위/ 다른 기둥 위
    if (
        y == 0
        or (graph[y - 1][x - 1] >= 2 or graph[y - 1][x] >= 2)
        or graph[y - 1][x] % 2 == 1
    ):
        return True
    return False


# 보가 조건 만족하는지 체크
def check_b(graph, x, y):
    # 한쪽 끝 부분이 기둥 위 / 양쪽 끝 부분이 다른 보와 동시에 연결
    if (
        graph[y - 1][x] % 2 == 1
        or graph[y - 1][x + 1] % 2 == 1
        or (graph[y - 1][x - 1] >= 2 and graph[y - 1][x + 1] >= 2)
    ):
        return True
    return False


def check_all(graph):
    avail_g = True
    avail_b = True

    for i in arr_g:
        avail_g = check_g(graph, i[0], i[1])
        if not avail_g:
            break
    for i in arr_b:
        avail_b = check_b(graph, i[0], i[1])
        if not avail_b:
            break

    if not avail_b or not avail_g:
        return False
    else:
        return True


# a 0 기둥 / 1 보
# b 0 삭제 / 1 설치
def build(graph, build_frame):
    for i in build_frame:
        x, y, a, b = i

        if b == 1:
            # 기둥 설치
            if a == 0:
                if check_g(graph, x, y):
                    graph[y][x] += 1
                    arr_g.append((x, y))
            # 보 설치
            else:
                if check_b(graph, x, y):
                    graph[y - 1][x] += 2
                    arr_b.append((x, y))
        else:
            # 기둥 삭제
            if a == 0:
                arr_g.remove((x, y))
                graph[y][x] -= 1
                removable = check_all(graph)

                if not removable:
                    arr_g.append((x, y))
                    graph[y][x] += 1
            # 보 삭제
            else:
                arr_b.remove((x, y))
                graph[y - 1][x] -= 2
                removable = check_all(graph)

                if not removable:
                    arr_b.append((x, y))
                    graph[y - 1][x] += 2


def print_result():
    result = []
    for i in arr_g:
        result.append([i[0], i[1], 0])
    for i in arr_b:
        result.append([i[0], i[1], 1])

    result.sort(key=lambda data: (data[0], data[1], -data[2]))

    return result


def solution(n, build_frame):
    answer = [[]]
    graph = [[0] * (n + 1) for _ in range(n)]  # 가로 n+1 * 세로 n

    build(graph, build_frame)
    answer = print_result()
    return answer


print(
    solution(
        5,
        [
            [0, 0, 0, 1],
            [2, 0, 0, 1],
            [4, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [2, 1, 1, 1],
            [3, 1, 1, 1],
            [2, 0, 0, 0],
            [1, 1, 1, 0],
            [2, 2, 0, 1],
        ],
    )
)
"""
"""
TC 1
5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
-> [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
TC 2
5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
-> [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
"""
