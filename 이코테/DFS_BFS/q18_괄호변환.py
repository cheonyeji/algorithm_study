# 이코테 DFS_BFS Q18 괄호변환
# https://programmers.co.kr/learn/courses/30/lessons/60058


def seperate(w):
    left = 0
    right = 0
    for i in range(len(w)):
        if w[i] == "(":
            left += 1
        else:
            right += 1
        # 개수가 같아 균형잡힌 경우
        if left == right:
            return w[: i + 1], w[i + 1 :]
        # 파이썬 슬라이싱 문법 복기
        # [:end] -> 시작점부터 특정위치(end-1)까지 가져오기
        # [start:] -> 특정시작위치(start)부터 끝까지 가져오기


def checkBalance(u):
    left = []
    for i in u:
        if i == "(":
            left.append(i)
        else:
            if not left:  # 비어있는 경우, 짝을 맞출 수 없는 경우이므로 False
                return False
            left.pop()  # 짝 맞추기
    # 모두 다 잘 들어갔다가 나온 경우, 짝이 맞는 것
    return True


def solution(p):
    # 1. 입력이 빈 문자열인 경우
    if not p:
        return ""
    # 2. 문자열 쪼개기
    u, v = seperate(p)
    # 3. 수행한 결과 문자열을 u에 이어붙인 후 반환
    if checkBalance(u):
        # 3-1. 올바른 괄호 문자열인 경우, 문자열 v에 대해 1단계부터 다시 수행
        return u + solution(v)
    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면
    else:
        # 4-1. 빈문자열+'('
        answer = "("
        # 4-2. 문자열 v에 대해 다시 1단계부터
        answer += solution(v)
        # 4-3.
        answer += ")"
        # 4-4. u의 첫번째와 마지막 문자를 제거, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙이기
        for i in u[1 : len(u) - 1]:
            if i == "(":  # 뒤집
                answer += ")"
            else:
                answer += "("
    # 4-5.
    return answer
