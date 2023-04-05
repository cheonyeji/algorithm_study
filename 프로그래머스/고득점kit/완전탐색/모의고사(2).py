# 2023-04-05
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 소요 시간 : 15:05 ~ 15:29 (20m)


def solution(answers):
    score = [0, 0, 0]
    answer = []
    students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    for i in range(len(answers)):
        for s in range(len(score)):
            if answers[i] == (students[s][i % len(students[s])]):
                score[s] += 1

    for s in range(len(score)):
        if max(score) == score[s]:
            answer.append(s + 1)
    return answer


print(solution([1, 2, 3, 4, 5]))
