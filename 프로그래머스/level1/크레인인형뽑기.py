# 2022-07-12
# 프로그래머스 lv1 - 크레인 인형 뽑기
# https://programmers.co.kr/learn/courses/30/lessons/17681
# 소요 시간 : 16:00 ~ 16:20 (20m)


def solution(board, moves):
    answer = 0

    N = len(board)  # NxN 크기의 격자

    bucket = []

    for m in moves:
        # board[i][m-1] 윗 행부터 체크
        for i in range(N):
            if board[i][m - 1] != 0:
                # 인형이 bucket의 가장 마지막 아이템과 같으면 pop
                if len(bucket) != 0 and bucket[-1] == board[i][m - 1]:
                    answer += 2
                    bucket.pop()
                # 아니면 넣기
                else:
                    bucket.append(board[i][m - 1])
                board[i][m - 1] = 0
                break

    return answer
