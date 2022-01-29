# 2021-01-26
# 이코테 ch12 구현 문제 Q10 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/5/lessons/60059


# 완탐을 원활하게 하기 위해 lock 리스트의 크기를 3배 이상으로 변경하기
# 자물쇠 리스트를 정중앙에 놓고 배치하면 계산이 수월

# 2차원 리스트를 90도 회전하는 함수
def rotate_matrix_by_90_degree(a):
    n = len(a)  # 행
    m = len(a[0])  # 열
    # 90도 회전한 후 결과값 다음 2차원 리스트(행, 열 Transpose)
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]  # n=행의 개수
    return result


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    origin_lock_len = len(new_lock) // 3
    for i in range(origin_lock_len, origin_lock_len * 2):
        for j in range(origin_lock_len, origin_lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 배열의 크기를 3배로
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 3배 크기의 자물쇠의 중앙에 기존 자물쇠 리스트 배치
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]  # 이때, n = 원래 자물쇠 길이

    # 4가지 방향에 대해 탐색
    for _ in range(4):
        key = rotate_matrix_by_90_degree(key)  # 열쇠 90도 회전
        # 회전시킨 열쇠를 자물쇠의 중앙부분에 합치기
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠 끼우기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 열쇠 돌기랑 자물쇠 홈이 맞는지 체크
                if check(new_lock):
                    return True

                # 안맞는 열쇠는 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


"""
TC -> true
key
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock
[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
"""
