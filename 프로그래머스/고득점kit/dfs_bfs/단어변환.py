# 2023-04-17
# 프로그래머스 고득점 kit - DFS/BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 소요 시간 : 1시간 넘게 못 풀어서 해설 참고

"""
모든 경우의 수를 싹 다 체크하되, 최소 몇 단계의 과정을 거쳐야하는지 변환 가능한지 체크 -> BFS
볼 필요 없는 경우의 수는 넘어가면 됨.
즉 한글자만 다른 단어만 계속해서 queue에 넣어주면서 경우의 수를 체크하면 됨
좋은 문제라고 생각.. 다시 풀어볼것
"""
from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])  # [단어, 깊이]
    visited = [0 for _ in range(len(words))]

    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            diff = 0  # 다른 글자수 체크용
            if not visited[i]:  # 확인x 단어면
                # 글자수가 1개만 다른지 체크해서 그럴 때만 q에 넣어주기
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff += 1
                if diff == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = 1

    return answer
