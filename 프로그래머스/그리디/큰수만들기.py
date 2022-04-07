# 2022-04-07
# 프로그래머스 고득점 kit 그리디 - 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883


def solution(number, k):
    answer = ""
    stack = []

    # 앞에서부터 값을 stack에 넣는데 그 값보다 스택에 들어있는 요소가 더 적으면 계속 pop
    # 같거나 크면 push
    # 만약 k <= 0이면 계속 push
    for i, val in enumerate(number):
        while len(stack) != 0 and int(stack[-1]) < int(val) and k > 0:
            stack.pop()
            k -= 1
        stack.append(val)

    # 제거 횟수를 다 사용하지 않은 경우
    # 뒤에서부터 k개 잘라줌 (마지막 테스트케이스에서 걸림)
    answer = stack[:-k] if k > 0 else stack[:]
    return "".join(answer)


print(solution("4177252841", 4))
